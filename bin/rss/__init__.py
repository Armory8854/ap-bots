import feedparser
import json

def rss_retrieve(rss_feed, rss_counter):
    global author
    global post
    global published_date
    global id_url
    parsed_rss_feed = feedparser.parse(rss_feed)
    parsed_rss_feed_full = parsed_rss_feed['entries'][rss_counter]
    author = parsed_rss_feed_full['author']
    post = parsed_rss_feed_full['title']
    published_date = parsed_rss_feed_full['published']
    id_url = parsed_rss_feed_full['id']
#    print(author + " " + post + " " + published_date + " " + id_url)
    return author, post, published_date, id_url
    
