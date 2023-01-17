# General Imports
import os
import configparser

# My imports
from database_functions import *
from rss import rss_retrieve
from ap import *

# File variables go here
config_file = "example.ini"
database_file = "test/test.db"

# Function like / function variables go here
#config = configparser.ConfigParser()
#config.read('./example.ini')

# Test vars here
rss_feed = "https://chimpsnw.org/blog/feed"
ap_instance = "https://iamterminally.online"
api_key = "YZVJNMU3MWYTN2Q4NS0ZOGY5LWJKYJETMWIXMTM2MMZIMWQ1"

# Max articles to retrive at a time
rss_counter = 0
rss_counter_ceiling = 5

while rss_counter < rss_counter_ceiling:
    rss_function = rss_retrieve(rss_feed, rss_counter)
    author, post, published_date, id_url = rss_function
    db_add(database_file, author, post, published_date, id_url)
    rss_counter = rss_counter + 1

new_posts = db_query(database_file)
new_posts_len = range(len(new_posts))
if len(new_posts) == 0:
    print("No new posts! Exiting...")
    quit
else:
    for i in new_posts_len:
        new_post_content = new_posts[i][1]
        new_post_uid = new_posts[i][4]
        new_post_link = new_posts[i][3]
        was_i_posted = new_posts[i][5]
        new_post(ap_instance, api_key, new_post_content, new_post_link, was_i_posted)
        db_posted(database_file, new_post_uid)
