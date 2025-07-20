book.delete()

# Confirm deletion
print(Book.objects.all())

# Output:
# <QuerySet []>
