# CRUD Operations using Django Shell

## Create
```python
from books.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
# Output: <Book: 1984 by George Orwell (1949)>

books = Book.objects.all()
for b in books:
    print(b.title, b.author, b.publication_year)
# Output:
# 1984 George Orwell 1949
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

updated_book = Book.objects.get(id=book.id)
print(updated_book)
# Output: <Book: Nineteen Eighty-Four by George Orwell (1949)>
book.delete()
print(Book.objects.all())
# Output: <QuerySet []>
cd