book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
updated_book = Book.objects.get(id=book.id)
print(updated_book)

# Output:
# <Book: Nineteen Eighty-Four by George Orwell (1949)>
