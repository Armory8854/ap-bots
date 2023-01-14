# General Imports
import os
import configparser

# My imports
from database_functions import db_add
from rss import rss_retrieve

# File variables go here
config_file = "example.ini"
database_file = "test/test.db"

# Function like / function variables go here
#config = configparser.ConfigParser()
#config.read('./example.ini')

# Test vars here
rss_feed = str("https://nitter.net/ChimpSanctuary/rss")

# Max articles to retrive at a time
rss_counter = 0
rss_counter_ceiling = 5

# Make the variables exist we plan on reassigning

while rss_counter < rss_counter_ceiling:
    rss_function = rss_retrieve(rss_feed, rss_counter)
    author, post, published_date, id_url = rss_function
    db_add(database_file, author, post, published_date, id_url)
    rss_counter = rss_counter + 1
