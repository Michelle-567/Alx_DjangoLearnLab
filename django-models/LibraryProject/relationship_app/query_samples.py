from relationship_app.models import Author, Book, Library

# ✅ Query all books by a specific author
def list_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"Books by '{author_name}':")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"Author with name '{author_name}' does not exist.")

# ✅ Query all books in a specific library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books = library.book_set.all()
        print(f"Books in library '{library_name}':")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"Library with name '{library_name}' does not exist.")

# Example test runs
list_books_by_author("George Orwell")
list_books_in_library("Main Library")
