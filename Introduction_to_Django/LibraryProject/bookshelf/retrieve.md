
# Retrieve a book by its primary key
book = Book.objects.get(pk=1)
print(book.title)
