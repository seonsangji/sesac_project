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
    total_user = cur.fetchone()[0]
    cur.close()
    return total_user

def get_users_per_page(page, count):
    offset = ( page - 1 ) * count
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users LIMIT ? OFFSET ? ', (count, offset))
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


    
