import os
import json
import feedparser
import sqlite3

rss_feed = str("https://nitter.net/ChimpSanctuary/rss")
parsed_rss_feed = feedparser.parse(rss_feed)

print(parsed_rss_feed)
print(json.dumps(parsed_rss_feed["entries"], indent=2))
#print(len(parsed_rss_feed))

def db_add():
    with sqlite3.connect('./test/test.db') as conn:
        conn = sqlite3.connect('./test/test.db')
        cur = conn.cursor()
        
