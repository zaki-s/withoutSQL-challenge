


import sqlite3
from connection import get_connection

def seed_database():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        authors = [("James",), ("Alice",), ("Robert",)]
        cursor.executemany("INSERT INTO authors (name) VALUES (?)", authors)

        magazines = [("Tech Monthly", "Technology"), ("Health Digest", "Health"), ("Business Weekly", "Business")]
        cursor.executemany("INSERT INTO magazines (name, category) VALUES (?, ?)", magazines)

        articles = [
            ("AI Revolution", 1, 1),
            ("Nutrition Myths", 2, 2),
            ("Stock Market Trends", 3, 3)
        ]
        cursor.executemany("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", articles)

        conn.commit()
        print("Database seeded successfully!")

    except sqlite3.Error as e:
        print(f"Database seeding failed: {e}")

    finally:
        conn.close()

if __name__ == "__main__":
    seed_database()
