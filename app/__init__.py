"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7p3u4dadc9vlvn4cg-a.oregon-postgres.render.com",
        database="mysql_a1z2",
        user="root",
        password="6G0uJkF7xcMdYUwHCc73nigrKxQpBHlL")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
