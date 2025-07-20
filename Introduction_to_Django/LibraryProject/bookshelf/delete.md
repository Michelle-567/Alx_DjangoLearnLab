# Delete Operation

```python
from bookshelf.models import Book

# Delete a book with title '1984'
book = Book.objects.get(title="1984")
book.delete()
