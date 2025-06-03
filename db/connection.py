


import sqlite3

def get_connection():
    """Returns a connection to the SQLite database."""
    return sqlite3.connect("articles.db")
