import sqlite3


def init_db():
    con = sqlite3.connect('data_basa.db')
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS words(
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            word TEXT,
            translate TEXT,
            )
    ''')
    con.commit()
    con.close()