from relationship_app.models import Author, Book

# Replace 'J.K. Rowling' with any author name you want to test
author_name = "J.K. Rowling"

# Get the Author instance
author = Author.objects.get(name=author_name)

# Get all books by that author
books_by_author = Book.objects.filter(author=author)

# Optional: print for debugging
for book in books_by_author:
    print(book.title)
