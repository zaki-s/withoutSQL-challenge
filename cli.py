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
    print("6. Exit")

    return input("\nChoose an option: ")

def main():
    while True:
        choice = menu()

        if choice == "1":
            name = input("Enter author name: ")
            author = Author.create(name)
            print(f"Created author: {author.name} (ID: {author.id})")

        elif choice == "2":
            name = input("Enter magazine name: ")
            category = input("Enter category: ")
            magazine = Magazine.create(name, category)
            print(f"Created magazine: {magazine.name} (Category: {magazine.category})")

        elif choice == "3":
            title = input("Enter article title: ")
            author_id = int(input("Enter author ID: "))
            magazine_id = int(input("Enter magazine ID: "))
            article = Article.create(title, author_id, magazine_id)
            print(f"Created article: {article.title}")

        elif choice == "4":
            author_id = int(input("Enter author ID: "))
            author = Author.find_by_id(author_id)
            print(f"Found author: {author.name}" if author else "Author not found.")

        elif choice == "5":
            author_id = int(input("Enter author ID: "))
            author = Author.find_by_id(author_id)
            if author:
                articles = author.all_articles()
                print(f"Articles by {author.name}: {articles}")
            else:
                print("Author not found.")

        elif choice == "6":
            print("Exiting CLI.")
            sys.exit()

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
