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



    
