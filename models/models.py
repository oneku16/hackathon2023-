import psycopg2 as pg
from faker import Faker
from random import randint


class DataBase:
    __slots__ = ('__connection', '__cursor', '__used_id')

    def __init__(self):
        self.__connection = self.__make_connection()
        self.__cursor = self.__connection.cursor()
        self.__used_id = set()

    @property
    def connection(self):
        return self.__connection

    @property
    def cursor(self):
        return self.__cursor

    @staticmethod
    def __make_connection():
        try:
            conn = pg.connect(
                host='localhost',
                database='postgres',
                port=5432,
                user='admin',
                password='secret'
            )
            print("Connection established.")
            return conn

        except Exception as err:
            raise err

    def build_base(self):
        self.__cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users(
                id SERIAL PRIMARY KEY,
                first_name VARCHAR(128),
                last_name VARCHAR(128),
                email VARCHAR(128),
                phone_number VARCHAR(64),
                birth_date DATE
            )''')
        self.__connection.commit()
        print("Table created.")

    def generate_random_user(self, number_of_users=1):
        fake = Faker()
        for _ in range(number_of_users):
            id = randint(10_000, 99_999)
            while id in self.__used_id:
                id = randint(10_000, 99_999)
            self.__used_id.add(id)
            first_name = fake.first_name()
            last_name = fake.last_name()
            email = fake.email()
            phone_number = fake.phone_number()
            birth_date = fake.date_of_birth(minimum_age=18, maximum_age=90)
            self.__cursor.execute(f"""
                    INSERT INTO Users (id, first_name, last_name, email, phone_number, birth_date) 
                    VALUES ({id}, '{first_name}', '{last_name}', '{email}', '{phone_number}', '{birth_date}');
                    """)
        self.__connection.commit()

    def get_users(self):
        self.__cursor.execute("""SELECT * FROM Users;""")
        users = self.__cursor.fetchall()

        for user in users:
            print(f'{user=}')

        self.__cursor.close()

    def clear_data_base(self):
        self.__cursor.execute("""DELETE FROM Users""")
        self.__connection.commit()
