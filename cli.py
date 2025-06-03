import sys
from models.author import Author
from models.magazine import Magazine
from models.article import Article

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
    print("12. Exit")
    return input("\nChoose an option: ")

def main():
    while True:
        choice = menu()

        if choice == "1":
            name = input("Enter author name: ").strip()
            if name:
                author = Author.create(name)
                print(f"Created author: {author.name} (ID: {author.id})")
            else:
                print("Invalid input.")

        elif choice == "2":
            name = input("Enter magazine name: ").strip()
            category = input("Enter category: ").strip()
            if name and category:
                magazine = Magazine.create(name, category)
                print(f"Created magazine: {magazine.name} (Category: {magazine.category})")
            else:
                print("Invalid input.")

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
                    print(f"Articles by {author.name}: {articles}")
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
                        print("Invalid input.")
                else:
                    print("Author not found.")
            except ValueError:
                print("Invalid input. Author ID must be a number.")

        elif choice == "7":
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
                        print("Invalid input.")
                else:
                    print("Magazine not found.")
            except ValueError:
                print("Invalid input. Magazine ID must be a number.")

        elif choice == "9":
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
                        print("Invalid input.")
                else:
                    print("Article not found.")
            except ValueError:
                print("Invalid input. Article ID must be a number.")

        elif choice == "11":
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
            print("Exiting CLI.")
            sys.exit()

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
