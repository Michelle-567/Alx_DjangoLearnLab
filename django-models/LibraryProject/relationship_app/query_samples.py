# query_samples.py

from relationship_app.models import Library

def list_books_in_library(library_name):
    try:
        # Get the library instance by name
        library = Library.objects.get(name=library_name)
        
        # Get all books related to this library
        books = library.books.all()

        # Print book titles
        print(f"Books in '{library_name}':")
        for book in books:
            print(f"- {book.title}")

    except Library.DoesNotExist:
        print(f"Library with name '{library_name}' does not exist.")

# Example usage
list_books_in_library("Central Library")
