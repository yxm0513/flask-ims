from sqlite3 import connect
from setting import *

def create_table():
    conn = connect(DATABASE)
    cur = conn.cursor()
    cur.execute('''drop table if exists ims''')
    cur.execute('''create table ims (id integer primary key autoincrement, name varchar(50), description text)''')
    conn.commit()
    cur.close()
    conn.close()

def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return ( rv[0] if rv else None) if one else rv

if __name__ == "__main__":
    create_db()