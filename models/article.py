import sqlite3
from db.connection import get_connection

class Article:
    def __init__(self, id, title, author_id, magazine_id):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    @classmethod
    def create(cls, title, author_id, magazine_id):
        """Creates a new Article."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?) RETURNING id", (title, author_id, magazine_id))
        article_id = cursor.fetchone()[0]
        conn.commit()
        conn.close()
        return cls(article_id, title, author_id, magazine_id)

    @classmethod
    def find_by_id(cls, article_id):
        """Finds an Article by ID."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id = ?", (article_id,))
        row = cursor.fetchone()
        conn.close()
        return cls(row[0], row[1], row[2], row[3]) if row else None

    def update_title(self, new_title):
        """Updates article title."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE articles SET title = ? WHERE id = ?", (new_title, self.id))
        conn.commit()
        conn.close()
        self.title = new_title

    def delete(self):
        """Deletes the article from the database."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM articles WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()
