import sqlite3, os

# def find_project_root(filename='mycrm.db'):
#     current_dir = os.path.abspath(__file__)
#     while True:
#         current_dir = os.path.dirname(current_dir)
#         if os.path.exists(os.path.join(current_dir, filename)):
#             return current_dir
#         if current_dir == os.path.dirname(current_dir):  # 루트 디렉토리까지 올라간 경우
#             raise FileNotFoundError(f"'{filename}' not found in any parent directory.")

# PROJECT_ROOT = find_project_root()
# DATABASE = os.path.join(PROJECT_ROOT, 'mycrm.db')

DATABASE = '../mycrm.db'


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


    
