import os
import sqlite3

def db_add(database_file, author, post, published_date, id_url):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tweets (author TEXT, post TEXT, published_date TEXT, id_url TEXT, uid INTEGER PRIMARY KEY AUTOINCREMENT, UNIQUE(id_url))")
    cursor.execute("INSERT OR IGNORE INTO tweets (author, post, published_date, id_url) VALUES (?, ?, ?, ?)",
                   (author, post, published_date, id_url))
    rows = cursor.execute("SELECT * FROM tweets").fetchall()
    print(rows)
    connection.commit()
    connection.close()

    
