# My imports
from database_functions import *
from rss import *
from ap import *

# General imports
import logging
from pathlib import Path

# File variables go here
working_dir = "/home/celer/git/ap-bots/"
config_file = working_dir + "test/example.ini"
database_file = working_dir + "test/test.db"
logging_file = working_dir + "test/example.log"

# Establish logging vars here
logging.basicConfig(filename=logging_file, encoding='utf-8', level=logging.DEBUG)

# Test vars here
rss_feed = ["https://chimpsnw.org/blog/feed", "https://www.youtube.com/feeds/videos.xml?channel_id=UCzJSKJKKhBlRGtAxc6T_g5w"]
rss_feed_range = range(len(rss_feed))
ap_instance = "https://iamterminally.online"
api_key = "YZVJNMU3MWYTN2Q4NS0ZOGY5LWJKYJETMWIXMTM2MMZIMWQ1"

# Max articles to retrive at a time
rss_counter = 0
rss_counter_ceiling = 5

# See if the database file exists. If not, create it
# If we can't create it for some reason, log an error
file_exists = Path(database_file).is_file()
if file_exists == False:
    logging.info("DB File does not exist. Attempting to create it")
    try:
        Path(database_file).touch()
    except:
        logging.critical("Cannot create Database file at " + database_file)
        quit

while rss_counter < rss_counter_ceiling:
    for x in rss_feed_range:
        logging.info("Pulling the last " + str(rss_counter_ceiling) + " articles from " + str(rss_feed_range) + "feeds")
        rss_function = rss_retrieve(rss_feed[x], rss_counter)
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
