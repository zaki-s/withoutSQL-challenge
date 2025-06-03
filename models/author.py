import sqlite3
from db.connection import get_connection

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def create(cls, name):
        """Creates a new Author and saves it to the database."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO authors (name) VALUES (?) RETURNING id", (name,))
        author_id = cursor.fetchone()[0]
        conn.commit()
        conn.close()
        return cls(author_id, name)

    @classmethod
    def find_by_id(cls, author_id):
        """Finds an Author by ID."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE id = ?", (author_id,))
        row = cursor.fetchone()
        conn.close()
        return cls(row[0], row[1]) if row else None

    def articles(self):
        """Returns all articles written by this author."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id = ?", (self.id,))
        return [row for row in cursor.fetchall()]

    def magazines(self):
        """Returns all unique magazines the author has contributed to."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.* FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        return [row for row in cursor.fetchall()]

    def update_name(self, new_name):
        """Updates the author's name in the database."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE authors SET name = ? WHERE id = ?", (new_name, self.id))
        conn.commit()
        conn.close()
        self.name = new_name  # Update local object

    def delete(self):
        """Deletes the author from the database."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM authors WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()
