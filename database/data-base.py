import sqlite3
import datetime

banco = sqlite3.connect('database/verificaFatos_database.db')

cursor = banco.cursor()

# tabela de usuarios
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT,
        password TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        last_login TIMESTAMP
    )
''')

# tabela de noticias
cursor.execute('''
    CREATE TABLE IF NOT EXISTS news (
        news_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT,
        content TEXT,
        created_at TIMESTAMP,
        is_verified BOOLEAN,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
''')

# tabela de histórico de login
cursor.execute('''
    CREATE TABLE IF NOT EXISTS login_history (
        history_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        login_time TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
''')

# tabela de histórico de consultas
cursor.execute('''
    CREATE TABLE IF NOT EXISTS search_history (
        search_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        search_term TEXT,
        search_time TIMESTAMP,
        results TEXT,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
''')

# Inserir um novo usuario
def insert_user(email, password):
    cursor.execute('''
        INSERT INTO users (email, password)
        VALUES (?, ?)
    ''', (email, password))
    banco.commit()

# Inserir uma nova noticia.
def insert_news(user_id, title, content):
    cursor.execute('''
        INSERT INTO news (user_id, title, content, created_at)
        VALUES (?, ?, ?, ?)
    ''', (user_id, title, content, datetime.datetime.now()))
    banco.commit()

def view_table(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    return cursor.fetchall()

banco.close()