import sqlite3
from db.connection import get_connection

class Magazine:
    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category

    @classmethod
    def create(cls, name, category):
        """Creates a new Magazine."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?) RETURNING id", (name, category))
        magazine_id = cursor.fetchone()[0]
        conn.commit()
        conn.close()
        return cls(magazine_id, name, category)

    @classmethod
    def find_by_id(cls, magazine_id):
        """Finds a Magazine by ID."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id = ?", (magazine_id,))
        row = cursor.fetchone()
        conn.close()
        return cls(row[0], row[1], row[2]) if row else None

    def update_name(self, new_name):
        """Updates magazine name."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE magazines SET name = ? WHERE id = ?", (new_name, self.id))
        conn.commit()
        conn.close()
        self.name = new_name

    def delete(self):
        """Deletes the magazine from the database."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM magazines WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()

    def all_articles(self):
        """Get all articles published in this magazine."""
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM articles WHERE magazine_id = ?", (self.id,))
        return cursor.fetchall()

