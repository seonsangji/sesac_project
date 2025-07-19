import sqlite3, os

filepath_now = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(os.path.dirname(filepath_now))
DATABASE = os.path.join(BASE_DIR, 'mycrm.db')

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def get_user_count():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM users')
    total = cur.fetchone()[0]
    cur.close()
    return total

def get_users_per_page(page, limit):
    offset = ( page - 1 ) * limit
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users LIMIT ? OFFSET ? ', (limit, offset))
    rows = cur.fetchall()
    users = [ dict(r) for r in rows ]
    cur.close()
    return users

def search_name_from_front(name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE Name LIKE ?', ( name + '%', ))
    rows = cur.fetchall()
    users = [ dict(r) for r in rows ]
    cur.close()
    return users

def search_lastname(name):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE Name LIKE ?', ( '%' + name , ))
    rows = cur.fetchall()
    users = [ dict(r) for r in rows ]
    cur.close()
    return users

def get_user_info(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users WHERE Id=?', (id,))
    user_dict = dict(cur.fetchone())
    cur.close()
    return user_dict

def get_order_info_by_userId(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT o.Id, o.OrderAt, o.StoreId FROM orders o
        JOIN users u ON o.UserId = u.Id
        WHERE u.Id = ?
        GROUP BY o.Id
        ORDER BY o.OrderAt DESC''', (id,))
    rows = cur.fetchall()
    order_dict = [dict(r) for r in rows]
    cur.close()
    return order_dict

    


    
