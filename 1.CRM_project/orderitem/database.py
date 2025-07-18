import sqlite3, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE = os.path.join(BASE_DIR,'mycrm.db')

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def get_orderitem_count():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM orderitems')
    total = cur.fetchone()[0]
    cur.close()
    return total

def get_orderitems_per_page(page, limit):
    offset = (page-1)*limit
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM orderitems LIMIT ? OFFSET ?', (limit, offset))
    rows = cur.fetchall()
    orderitems = [dict(r) for r in rows]
    cur.close()
    return orderitems

def get_orderitem_info_by_orderId(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT oi.Id, oi.OrderId, oi.ItemId, i.Name FROM items i
        JOIN orderitems oi ON i.Id = oi.ItemId
        WHERE oi.OrderId = ?
	    GROUP BY oi.ItemId
    ''', (id,))
    rows = cur.fetchall()
    orderitems_dict = [dict(r) for r in rows]
    print(orderitems_dict)
    cur.close()
    return orderitems_dict


