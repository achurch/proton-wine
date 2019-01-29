/*
 * Implementation of the Microsoft Installer (msi.dll)
 *
 * Copyright 2002-2004 Mike McCormack for CodeWeavers
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA
 */

#include <stdarg.h>

#include "windef.h"
#include "winbase.h"
#include "winerror.h"
#include "wine/debug.h"
#include "msi.h"
#include "msiquery.h"
#include "objbase.h"
#include "objidl.h"
#include "msipriv.h"
#include "winnls.h"

#include "query.h"

WINE_DEFAULT_DEBUG_CHANNEL(msidb);


/* below is the query interface to a table */

typedef struct tagMSISELECTVIEW
{
    MSIVIEW        view;
    MSIDATABASE   *db;
    MSIVIEW       *table;
    UINT           num_cols;
    UINT           max_cols;
    UINT           cols[1];
} MSISELECTVIEW;

static UINT SELECT_fetch_int( struct tagMSIVIEW *view, UINT row, UINT col, UINT *val )
{
    MSISELECTVIEW *sv = (MSISELECTVIEW*)view;

    TRACE("%p %d %d %p\n", sv, row, col, val );

    if( !sv->table )
         return ERROR_FUNCTION_FAILED;

    if( !col || col > sv->num_cols )
         return ERROR_FUNCTION_FAILED;

    col = sv->cols[ col - 1 ];
    if( !col )
    {
        *val = 0;
        return ERROR_SUCCESS;
    }
    return sv->table->ops->fetch_int( sv->table, row, col, val );
}

static UINT SELECT_fetch_stream( struct tagMSIVIEW *view, UINT row, UINT col, IStream **stm)
{
    MSISELECTVIEW *sv = (MSISELECTVIEW*)view;

    TRACE("%p %d %d %p\n", sv, row, col, stm );

    if( !sv->table )
         return ERROR_FUNCTION_FAILED;

    if( !col || col > sv->num_cols )
         return ERROR_FUNCTION_FAILED;

    col = sv->cols[ col - 1 ];
    if( !col )
    {
        *stm = NULL;
        return ERROR_SUCCESS;
    }
    return sv->table->ops->fetch_stream( sv->table, row, col, stm );
}

static UINT SELECT_set_row( struct tagMSIVIEW *view, UINT row, MSIRECORD *rec, UINT mask )
{
    MSISELECTVIEW *sv = (MSISELECTVIEW*)view;
    UINT i, expanded_mask = 0, r = ERROR_SUCCESS, col_count = 0;
    MSIRECORD *expanded;

    TRACE("%p %d %p %08x\n", sv, row, rec, mask );

    if ( !sv->table )
         return ERROR_FUNCTION_FAILED;

    /* test if any of the mask bits are invalid */
    if ( mask >= (1<<sv->num_cols) )
        return ERROR_INVALID_PARAMETER;

    /* find the number of columns in the table below */
    r = sv->table->ops->get_dimensions( sv->table, NULL, &col_count );
    if( r )
        return r;

    /* expand the record to the right size for the underlying table */
    expanded = MSI_CreateRecord( col_count );
    if ( !expanded )
        return ERROR_FUNCTION_FAILED;

    /* move the right fields across */
    for ( i=0; i<sv->num_cols; i++ )
    {
        r = MSI_RecordCopyField( rec, i+1, expanded, sv->cols[ i ] );
        if (r != ERROR_SUCCESS)
            break;
        expanded_mask |= (1<<(sv->cols[i]-1));
    }

    /* set the row in the underlying table */
    if (r == ERROR_SUCCESS)
        r = sv->table->ops->set_row( sv->table, row, expanded, expanded_mask );

    msiobj_release( &expanded->hdr );
    return r;
}

static UINT SELECT_insert_row( struct tagMSIVIEW *view, MSIRECORD *record, UINT row, BOOL temporary )
{
    MSISELECTVIEW *sv = (MSISELECTVIEW*)view;
    UINT i, table_cols, r;
    MSIRECORD *outrec;

    TRACE("%p %p\n", sv, record );

    if ( !sv->table )
        return ERROR_FUNCTION_FAILED;

    /* rearrange the record to suit the table */
    r = sv->table->ops->get_dimensions( sv->table, NULL, &table_cols );
    if (r != ERROR_SUCCESS)
        return r;

    outrec = MSI_CreateRecord( table_cols + 1 );

    for (i=0; i<sv->num_cols; i++)
    {
        r = MSI_RecordCopyField( record, i+1, outrec, sv->cols[i] );
        if (r != ERROR_SUCCESS)
            goto fail;
    }

    r = sv->table->ops->insert_row( sv->table, outrec, row, temporary );

fail:
    msiobj_release( &outrec->hdr );

    return r;
}

static UINT SELECT_execute( struct tagMSIVIEW *view, MSIRECORD *record )
{
    MSISELECTVIEW *sv = (MSISELECTVIEW*)view;

    TRACE("%p %p\n", sv, record);

    if( !sv->table )
         return ERROR_FUNCTION_FAILED;

    return sv->table->ops->execute( sv->table, record );
}

static UINT SELECT_close( struct tagMSIVIEW *view )
{
    MSISELECTVIEW *sv = (MSISELECTVIEW*)view;

    TRACE("%p\n", sv );

    if( !sv->table )
         return ERROR_FUNCTION_FAILED;

    return sv->table->ops->close( sv->table );
}

static UINT SELECT_get_dimensions( struct tagMSIVIEW *view, UINT *rows, UINT *cols )
{
    MSISELECTVIEW *sv = (MSISELECTVIEW*)view;

    TRACE("%p %p %p\n", sv, rows, cols );

    if( !sv->table )
         return ERROR_FUNCTION_FAILED;

    if( cols )
        *cols = sv->num_cols;

    return sv->table->ops->get_dimensions( sv->table, rows, NULL );
}

static UINT SELECT_get_column_info( struct tagMSIVIEW *view, UINT n, LPCWSTR *name,
                                    UINT *type, BOOL *temporary, LPCWSTR *table_name )
{
    MSISELECTVIEW *sv = (MSISELECTVIEW*)view;

    TRACE("%p %d %p %p %p %p\n", sv, n, name, type, temporary, table_name );

    if( !sv->table )
         return ERROR_FUNCTION_FAILED;

    if( !n || n > sv->num_cols )
         return ERROR_FUNCTION_FAILED;

    n = sv->cols[ n - 1 ];
    if( !n )
    {
        if (name) *name = szEmpty;
        if (type) *type = MSITYPE_UNKNOWN | MSITYPE_VALID;
        if (temporary) *temporary = FALSE;
        if (table_name) *table_name = szEmpty;
        return ERROR_SUCCESS;
    }
    return sv->table->ops->get_column_info( sv->table, n, name,
                                            type, temporary, table_name );
}

static UINT msi_select_update(struct tagMSIVIEW *view, MSIRECORD *rec, UINT row)
{
    MSISELECTVIEW *sv = (MSISELECTVIEW*)view;
    UINT r, i, col, type, val;
    IStream *stream;
    LPCWSTR str;

    for (i = 0; i < sv->num_cols; i++)
    {
        col = sv->cols[i];

        r = SELECT_get_column_info(view, i + 1, NULL, &type, NULL, NULL);
        if (r != ERROR_SUCCESS)
        {
            ERR("Failed to get column information: %d\n", r);
            return r;
        }

        if (MSITYPE_IS_BINARY(type))
        {
            if (MSI_RecordGetIStream(rec, i + 1, &stream))
                return ERROR_FUNCTION_FAILED;
            r = sv->table->ops->set_stream(sv->table, row, col, stream);
        }
        else if (type & MSITYPE_STRING)
        {
            int len;
            str = msi_record_get_string(rec, i + 1, &len);
            r = sv->table->ops->set_string(sv->table, row, col, str, len);
        }
        else
        {
            val = MSI_RecordGetInteger(rec, i + 1);
            r = sv->table->ops->set_int(sv->table, row, col, val);
        }

        if (r != ERROR_SUCCESS)
        {
            ERR("Failed to modify record: %d\n", r);
            return r;
        }
    }

    return ERROR_SUCCESS;
}

static UINT SELECT_modify( struct tagMSIVIEW *view, MSIMODIFY eModifyMode,
                           MSIRECORD *rec, UINT row )
{
    MSISELECTVIEW *sv = (MSISELECTVIEW*)view;

    TRACE("%p %d %p %d\n", sv, eModifyMode, rec, row );

    if( !sv->table )
         return ERROR_FUNCTION_FAILED;

    if (eModifyMode == MSIMODIFY_UPDATE)
        return msi_select_update(view, rec, row);

    return sv->table->ops->modify( sv->table, eModifyMode, rec, row );
}

static UINT SELECT_delete( struct tagMSIVIEW *view )
{
    MSISELECTVIEW *sv = (MSISELECTVIEW*)view;

    TRACE("%p\n", sv );

    if( sv->table )
        sv->table->ops->delete( sv->table );
    sv->table = NULL;

    msi_free( sv );

    return ERROR_SUCCESS;
}

static const MSIVIEWOPS select_ops =
{
    SELECT_fetch_int,
    SELECT_fetch_stream,
    NULL,
    NULL,
    NULL,
    SELECT_set_row,
    SELECT_insert_row,
    NULL,
    SELECT_execute,
    SELECT_close,
    SELECT_get_dimensions,
    SELECT_get_column_info,
    SELECT_modify,
    SELECT_delete,
    NULL,
    NULL,
    NULL,
    NULL,
    NULL,
};

static UINT SELECT_AddColumn( MSISELECTVIEW *sv, LPCWSTR name,
                              LPCWSTR table_name )
{
    UINT r, n;
    MSIVIEW *table;

    TRACE("%p adding %s.%s\n", sv, debugstr_w( table_name ),
          debugstr_w( name ));

    if( sv->view.ops != &select_ops )
        return ERROR_FUNCTION_FAILED;

    table = sv->table;
    if( !table )
        return ERROR_FUNCTION_FAILED;
    if( !table->ops->get_dimensions )
        return ERROR_FUNCTION_FAILED;
    if( !table->ops->get_column_info )
        return ERROR_FUNCTION_FAILED;

    if( sv->num_cols >= sv->max_cols )
        return ERROR_FUNCTION_FAILED;

    if ( !name[0] ) n = 0;
    else
    {
        r = VIEW_find_column( table, name, table_name, &n );
        if( r != ERROR_SUCCESS )
            return r;
    }

    sv->cols[sv->num_cols] = n;
    TRACE("Translating column %s from %d -> %d\n", 
          debugstr_w( name ), sv->num_cols, n);

    sv->num_cols++;

    return ERROR_SUCCESS;
}

static int select_count_columns( const column_info *col )
{
    int n;
    for (n = 0; col; col = col->next)
        n++;
    return n;
}

UINT SELECT_CreateView( MSIDATABASE *db, MSIVIEW **view, MSIVIEW *table,
                        const column_info *columns )
{
    MSISELECTVIEW *sv = NULL;
    UINT count = 0, r = ERROR_SUCCESS;

    TRACE("%p\n", sv );

    count = select_count_columns( columns );

    sv = msi_alloc_zero( FIELD_OFFSET( MSISELECTVIEW, cols[count] ));
    if( !sv )
        return ERROR_FUNCTION_FAILED;
    
    /* fill the structure */
    sv->view.ops = &select_ops;
    sv->db = db;
    sv->table = table;
    sv->num_cols = 0;
    sv->max_cols = count;

    while( columns )
    {
        r = SELECT_AddColumn( sv, columns->column, columns->table );
        if( r )
            break;
        columns = columns->next;
    }

    if( r == ERROR_SUCCESS )
        *view = &sv->view;
    else
        msi_free( sv );

    return r;
}
