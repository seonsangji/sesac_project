import sqlite3, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE = os.path.join(BASE_DIR, 'mycrm.db')

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def get_order_count():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM orders')
    total = cur.fetchone()[0]
    cur.close()
    return total

def get_orders_per_page(page, limit):
    offset = (page - 1) * limit
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM orders LIMIT ? OFFSET ?', (limit, offset))
    rows = cur.fetchall()
    orders = [dict(r) for r in rows]
    cur.close()
    return orders

def get_order_info(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM orders WHERE Id = ?', (id,))
    order = dict(cur.fetchone())
    cur.close()
    return order
