from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from api.models import Book

class BookAPITestCase(APITestCase):

    from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from .models import Book, Author
from rest_framework import status

class BookAPITestCase(APITestCase):

    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.admin_user = User.objects.create_superuser(username="admin", password="admin123")

        # Create an author instance ✅
        self.author = Author.objects.create(name="Author A")

        # Now create a book using the Author instance
        self.book = Book.objects.create(
            title="Test Book",
            author=self.author,   # ✅ use Author instance, not string
            published_date="2024-01-01"
        )

        # Endpoints
        self.list_url = "/books/"
        self.detail_url = f"/books/{self.book.id}/"


    # ------------------ CRUD TESTS ------------------ #
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book.title)

    def test_create_book_authenticated(self):
        data = {"title": "New Book", "author": "Author B", "published_date": "2024-02-01"}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        client = APIClient()
        data = {"title": "Unauthorized Book", "author": "Author C", "published_date": "2024-03-01"}
        response = client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        data = {"title": "Updated Book", "author": "Author A", "published_date": "2024-01-01"}
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    def test_delete_book_admin_only(self):
        response = self.admin_client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_delete_book_non_admin_forbidden(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # ------------------ FILTERING, SEARCH & ORDERING ------------------ #
    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url, {"author": "Author A"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book["author"] == "Author A" for book in response.data))

    def test_search_books_by_title(self):
        response = self.client.get(self.list_url, {"search": "Test"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_order_books_by_date(self):
        response = self.client.get(self.list_url, {"ordering": "published_date"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dates = [book["published_date"] for book in response.data]
        self.assertEqual(dates, sorted(dates))

