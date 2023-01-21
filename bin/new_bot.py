# My imports
from database_functions import *
from rss import *
from ap import *

# File variables go here
database_file = "test/test.db"
ap_instance = "https://iamterminally.online"
app_name = input("Enter what you want to name your app: ")

new_app(ap_instance,app_name)
