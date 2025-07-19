import sqlite3, os

filepath_now = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(filepath_now))
DATABASE = os.path.join(BASE_DIR, 'mycrm.db')

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def get_items():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM items')
    rows = cur.fetchall()
    total_items = [dict(r) for r in rows]
    cur.close()
    return total_items

def get_item_info(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM items WHERE Id=?', (id,))
    item_dict = dict(cur.fetchone())
    cur.close()
    return item_dict

def get_item_rev(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''SELECT 
    strftime('%Y-%m', o.OrderAt) AS Month, 
    SUM(i.unitPrice) AS  TotalRevenue,
    COUNT(oi.ItemId) AS ItemCount
    FROM orderitems oi
    JOIN orders o ON oi.OrderId = o.Id
    JOIN items i ON oi.ItemId = i.Id
    WHERE oi.ItemId = ?
    GROUP BY Month
    ORDER BY Month 
    ''', (id,))
    rows = cur.fetchall()
    rev_dict = [dict(r) for r in rows]
    cur.close()
    return rev_dict