from config import *
from pyg import Pyg


class Database:
    def __init__(self):
        self._db = Pyg(
            host=POSTGRES_HOST,
            port=POSTGRES_PORT,
            database=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
        )

        self._setup_db()

    def _setup_db(self):
        self._db.run_query(f'''CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(150) NOT NULL,
            email VARCHAR(50) NOT NULL UNIQUE,
            password VARCHAR(100) NOT NULL
        );''')
    
    def add_user(self, data):
        return self._db.run_query('''INSERT INTO users
            (name,email,password)
            VALUES (%s,%s,%s)
            RETURNING id
        ;''', [data['name'], data['email'], data['password']])
    
    def get_all_users(self):
        users = self._db.run_query('SELECT * FROM users;') or []
        users = map(lambda user: {'id': user[0], 'name': user[1], 'email': user[2]}, users)
        return list(users)
    