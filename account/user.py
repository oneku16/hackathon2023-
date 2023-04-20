from sqlite3 import connect
from config import DATE_BASE
from tools.image_tools import save_image


def sign_up(first_name, last_name, email, password, image=None):
    data_base = connect(DATE_BASE)
    data_base.execute('''CREATE TABLE IF NOT EXISTS users
                     (email TEXT PRIMARY KEY,
                     user_name TEXT NOT NULL,
                     last_name TEXT NOT NULL,
                     password TEXT NOT NULL);''')

    data_base.execute("INSERT INTO users (email, user_name, last_name, password) VALUES (?, ?, ?, ?)",
                      (email, first_name, last_name, password))
    data_base.commit()

    data_base = connect('users.db')
    data_base.close()
    if image:
        save_image(image=image, email=email)


def sign_in(email, password):
    data_base = connect(DATE_BASE)
    cursor = data_base.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
    row = cursor.fetchone()

    data_base.close()

    return {'status': False} if row is None else {'status': True}
