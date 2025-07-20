import sqlite3, os

filepath_now = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(filepath_now))
DATABASE = os.path.join(BASE_DIR, 'mycrm.db')

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def get_store_count():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM stores')
    total = cur.fetchone()[0]
    cur.close()
    return total

def get_stores_per_page(page, limit):
    offset = ( page - 1 ) * limit
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM stores LIMIT ? OFFSET ? ', (limit, offset))
    rows = cur.fetchall()
    stores = [ dict(r) for r in rows ]
    cur.close()
    return stores

def get_store_info(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM stores WHERE Id=?', (id,))
    store_dict = dict(cur.fetchone())
    cur.close()
    return store_dict

def get_store_rev(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT
        strftime('%Y-%m', o.OrderAt) AS Month,
        SUM(i.UnitPrice) AS Rev,
        COUNT(oi.Id) AS OrderitemCount
        FROM orders o 
        JOIN orderitems oi ON o.Id = oi.OrderId
        JOIN items i ON oi.ItemId = i.Id
        WHERE o.StoreId = ?
        GROUP BY Month
        ORDER BY Month
            ''',(id,))
    rows = cur.fetchall()
    rev_dict = [dict(r) for r in rows]
    cur.close()
    return rev_dict
    
def get_user_list_by_storeId(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT 
        u.Id AS UserId, 
        u.Name AS UserName, 
        COUNT(o.Id) AS Frequency
        FROM orders o
        JOIN users u ON o.UserId = u.Id
        JOIN stores s ON o.StoreId = s.Id
        WHERE s.Id = ?
        GROUP BY u.Id
        ORDER BY Frequency DESC
        LIMIT 10''', (id,))
    rows = cur.fetchall()
    user_dict = [dict(r) for r in rows]
    cur.close()
    return user_dict

def get_store_rev_for_month(month, id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT
        strftime('%Y-%m-%d', o.OrderAt) AS Day,
        SUM(i.UnitPrice) AS Rev,
        COUNT(oi.Id) AS OrderitemCount
        FROM orders o 
        JOIN orderitems oi ON o.Id = oi.OrderId
        JOIN items i ON oi.ItemId = i.Id
        WHERE o.StoreId = ? AND strftime('%Y-%m', o.OrderAt) = ?	
        GROUP BY Day
        ORDER BY Day ASC''', (id,month))
    rows = cur.fetchall()
    rev_month_dict = [dict(r) for r in rows]
    cur.close()
    return rev_month_dict

def get_user_list_by_storeId_for_month(month, id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT 
        u.Id AS UserId, 
        u.Name AS UserName, 
        COUNT(o.Id) AS Frequency
        FROM orders o
        JOIN users u ON o.UserId = u.Id
        JOIN stores s ON o.StoreId = s.Id
        WHERE s.Id = ? AND strftime('%Y-%m',o.OrderAt) = ?
        GROUP BY u.Id
        LIMIT 10''',(id, month))
    rows = cur.fetchall()
    user_month_dict = [dict(r) for r in rows]
    cur.close()
    return user_month_dict






    
