import sys
import sqlite3
from models.author import Author
from models.magazine import Magazine
from models.article import Article

DB_NAME = "articles.db"

def menu():
    print("\n1. Create Author")
    print("2. Create Magazine")
    print("3. Create Article")
    print("4. Find Author by ID")
    print("5. List Articles by Author")
    print("6. Update Author Name")
    print("7. Delete Author")
    print("8. Update Magazine Name")
    print("9. Delete Magazine")
    print("10. Update Article Title")
    print("11. Delete Article")
    print("12. List All Authors")
    print("13. List All Magazines")
    print("14. List All Articles")
    print("15. Exit")
    return input("\nChoose an option: ")

def get_db_connection():
    return sqlite3.connect(DB_NAME)

def list_authors():
    print("Starting list_authors()...")  # Debugging line

    try:
        conn = sqlite3.connect("articles.db")
        cursor = conn.cursor()
        print("Connected to database.")  # Debugging line

        cursor.execute("SELECT id, name FROM authors")
        authors = cursor.fetchall()
        print("Query executed.")  # Debugging line

        conn.close()
        print("Database connection closed.")  # Debugging line

        if not authors:
            print("No authors found.")
            return

        print("\nAvailable Authors:")
        for author_id, author_name in authors:
            print(f"{author_id} - {author_name}")

    except Exception as e:
        print(f"Error retrieving authors: {e}")



def list_magazines():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM magazines")
    magazines = cursor.fetchall()
    conn.close()

    if not magazines:
        print("No magazines found.")
        return

    print("\nAvailable Magazines:")
    for magazine_id, magazine_name in magazines:
        print(f"{magazine_id} - {magazine_name}")

def list_articles():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM articles")
    articles = cursor.fetchall()
    conn.close()

    if not articles:
        print("No articles found.")
        return

    print("\nAvailable Articles:")
    for article_id, article_title in articles:
        print(f"{article_id} - {article_title}")

def main():
    while True:
        choice = menu()

        if choice == "1":
            name = input("Enter author name: ").strip()
            if name:
                author = Author.create(name)
                print(f"Created author: {author.name} (ID: {author.id})")

        elif choice == "2":
            name = input("Enter magazine name: ").strip()
            category = input("Enter category: ").strip()
            if name and category:
                magazine = Magazine.create(name, category)
                print(f"Created magazine: {magazine.name} (Category: {magazine.category})")

        elif choice == "3":
            title = input("Enter article title: ").strip()
            try:
                author_id = int(input("Enter author ID: "))
                magazine_id = int(input("Enter magazine ID: "))
                article = Article.create(title, author_id, magazine_id)
                print(f"Created article: {article.title}")
            except ValueError:
                print("Invalid input. Author ID and Magazine ID must be numbers.")

        elif choice == "4":
            try:
                author_id = int(input("Enter author ID: "))
                author = Author.find_by_id(author_id)
                print(f"Found author: {author.name}" if author else "Author not found.")
            except ValueError:
                print("Invalid input. Author ID must be a number.")

        elif choice == "5":
            try:
                author_id = int(input("Enter author ID: "))
                author = Author.find_by_id(author_id)
                if author:
                    articles = author.all_articles()
                    print(f"Articles by {author.name}:")
                    for article in articles:
                        print(f"- {article[0]} ({article[1]})")
                else:
                    print("Author not found.")
            except ValueError:
                print("Invalid input. Author ID must be a number.")

        elif choice == "6":
            try:
                author_id = int(input("Enter author ID to update: "))
                author = Author.find_by_id(author_id)
                if author:
                    new_name = input("Enter new name: ").strip()
                    if new_name:
                        author.update_name(new_name)
                        print(f"Updated author name to {author.name}")
                else:
                    print("Author not found.")
            except ValueError:
                print("Invalid input. Author ID must be a number.")

        elif choice == "7":
            list_authors()
            try:
                author_id = int(input("Enter author ID to delete: "))
                author = Author.find_by_id(author_id)
                if author:
                    author.delete()
                    print("Author deleted.")
                else:
                    print("Author not found.")
            except ValueError:
                print("Invalid input. Author ID must be a number.")

        elif choice == "8":
            try:
                magazine_id = int(input("Enter magazine ID to update: "))
                magazine = Magazine.find_by_id(magazine_id)
                if magazine:
                    new_name = input("Enter new name: ").strip()
                    if new_name:
                        magazine.update_name(new_name)
                        print(f"Updated magazine name to {magazine.name}")
                else:
                    print("Magazine not found.")
            except ValueError:
                print("Invalid input. Magazine ID must be a number.")

        elif choice == "9":
            list_magazines()
            try:
                magazine_id = int(input("Enter magazine ID to delete: "))
                magazine = Magazine.find_by_id(magazine_id)
                if magazine:
                    magazine.delete()
                    print("Magazine deleted.")
                else:
                    print("Magazine not found.")
            except ValueError:
                print("Invalid input. Magazine ID must be a number.")

        elif choice == "10":
            try:
                article_id = int(input("Enter article ID to update: "))
                article = Article.find_by_id(article_id)
                if article:
                    new_title = input("Enter new title: ").strip()
                    if new_title:
                        article.update_title(new_title)
                        print(f"Updated article title to {article.title}")
                else:
                    print("Article not found.")
            except ValueError:
                print("Invalid input. Article ID must be a number.")

        elif choice == "11":
            list_articles()
            try:
                article_id = int(input("Enter article ID to delete: "))
                article = Article.find_by_id(article_id)
                if article:
                    article.delete()
                    print("Article deleted.")
                else:
                    print("Article not found.")
            except ValueError:
                print("Invalid input. Article ID must be a number.")

        elif choice == "12":
            list_authors()

        elif choice == "13":
            list_magazines()

        elif choice == "14":
            list_articles()

        elif choice == "15":
            print("Exiting CLI.")
            sys.exit()

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
