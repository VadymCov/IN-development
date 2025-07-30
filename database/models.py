import sqlite3


def init_db():
    con = sqlite3.connect('data_base.db')
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS words(
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            word TEXT,
            word_usertrans TEXT,
            word_googltrans TEXT,
            )
    ''')
    con.commit()
    con.close()