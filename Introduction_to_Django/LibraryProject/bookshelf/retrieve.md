
# Retrieve Operation

```python
# Retrieve a book with title '1984'
book = Book.objects.get(title="1984")
print(book.title)
