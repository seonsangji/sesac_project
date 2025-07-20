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

def get_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    total = [dict(r) for r in cur.fetchall()]
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

def get_user_behavior(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('''
        SELECT 
        s.Name AS StoreName,
        COUNT(s.Id) AS VisitCount
        FROM orders o 
        JOIN stores s ON o.StoreId = s.Id
        JOIN users u ON o.UserId = u.Id
        WHERE u.Id = ?
        GROUP BY s.Id
        ORDER BY VisitCount DESC 
        LIMIT 5''', (id, ))
    visit_dict = [dict(row) for row in cur.fetchall()] 
    cur.execute('''
        SELECT
        i.Name AS ItemName,
        COUNT(oi.Id) AS OrderCount
        FROM orderitems oi
        JOIN orders o ON oi.OrderId = o.Id
        JOIN items i ON oi.ItemId = i.Id
        JOIN users u ON o.UserId = u.Id
        WHERE u.Id = ?
        GROUP BY i.Id
        ORDER BY OrderCount DESC, ItemName ASC
        LIMIT 5''', (id,))
    ordercount_dict = [dict(row) for row in cur.fetchall()]
    cur.close()

    return visit_dict, ordercount_dict



    


    
