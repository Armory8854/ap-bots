import sqlite3
import logging
from pathlib import Path

# Define connection and cursor objects.
logging.info("Adding new posts to the database...")

def db_add(database_file, author, post, published_date, id_url):
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS tweets (author TEXT, post TEXT, published_date TEXT, id_url TEXT, uid INTEGER PRIMARY KEY AUTOINCREMENT, posted INTEGER, UNIQUE(id_url))")

    cursor.execute("INSERT OR IGNORE INTO tweets (author, post, published_date, id_url, posted) VALUES (?, ?, ?, ?, ?)",
                   (author, post, published_date, id_url, "0"))
    connection.commit()
    connection.close()

def db_query(database_file):
    logging.info("Searhing for posts to make...")
    global new_posts
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    new_posts = cursor.execute('SELECT * FROM tweets WHERE posted=0').fetchall()
    return new_posts
    connection.close()

def db_posted(database_file, new_post_uid):
    print("Updating toots as posted in the database...")
    connection = sqlite3.connect(database_file)
    cursor = connection.cursor()
    just_posted = cursor.execute("UPDATE tweets SET posted=1 WHERE uid=?", [new_post_uid])
    new_posted = cursor.execute('SELECT * FROM tweets WHERE posted=1').fetchall()
    connection.commit()
    connection.close()
