import sqlite3

# try:
#     connection = sqlite3.connect('sqlite.db')
# except sqlite3.DatabaseError:
#     print('Возникла ошибка при подключении к бд')
# finally:
#     connection.close()
class User:
    def __init__(self, name: str, surname: str, age: int, gender: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

def add_new_user(cur: sqlite3.Cursor, user: User):
    command = """
    INSERT INTO users (name, surname, age, gender) VALUES (
    ?, ?, ?, ?    
    )
    """
    cur.execute(command, (user.name, user.surname, user.age, user.gender))

def get_all_users(cur: sqlite3.Cursor):
    command = """
    SELECT * FROM users
    """
    result = cur.execute(command)
    return result.fetchall()

def create_user_table(cur: sqlite3.Cursor):
    command = """
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    age INTEGER,
    gender TEXT);
    """
    cur.execute(command)

def get_user(cur: sqlite3.Cursor, user_id: int):
    command = """
    SELECT * FROM users WHERE id = ?
    """

    result = cur.execute(command, (user_id,))
    return result.fetchall()

def upd_user(cur: sqlite3.Cursor, name: str, user_id: int):
    command = """
    UPDATE users SET name = ? WHERE id = ?
    """

    cur.execute(command, (name, user_id))

def delete(cur: sqlite3.Cursor):
    command = """
    DELETE FROM 
    """
if __name__ == "__main__":
    with sqlite3.connect('sqlite.db') as connection:
        cursor = connection.cursor()
        create_user_table(cursor)
        user = User(name="Максим", surname="Андрианов", age=15, gender="male")
        add_new_user(cursor, user=user)
        users = get_all_users(cursor)
        print(users)
        users = get_user(cursor, 1)
        print(users)
        upd_user(cursor, 'Евгений', 86)
        user = get_user(cursor, 1)
        print(user)