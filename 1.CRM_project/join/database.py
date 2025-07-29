import sqlite3, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASE = os.path.join(BASE_DIR, 'mycrm.db')

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def create_user(id, name, gender, age, birthdate, address):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('INSERT INTO users (Id, Name, Gender, Age, Birthdate, Address) VALUES (?,?,?,?,?,?) ', (id, name, gender, age, birthdate, address))
    conn.commit()
    conn.close()
    return print(f"{name} 돈 쓸 준비 완료!")