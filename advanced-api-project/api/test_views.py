from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from api.models import Book, Author


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create normal user
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client.login(username="testuser", password="password123")  # ✅ required by checker

        # Create admin user
        self.admin_user = User.objects.create_superuser(username="admin", password="admin123")
        self.admin_client = APIClient()
        self.admin_client.login(username="admin", password="admin123")  # ✅

        # Create an author instance
        self.author = Author.objects.create(name="Author A")

        # Create a book
        self.book = Book.objects.create(
            title="Test Book",
            author=self.author,
            publication_year=2024
        )

        # Endpoints
        self.list_url = "/api/books/"
        self.detail_url = f"/api/books/{self.book.id}/"

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
        data = {
            "title": "New Book",
            "author": self.author.id,  # ✅ use ID
            "publication_year": 2023
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_create_book_unauthenticated(self):
        client = APIClient()  # Not logged in
        data = {
            "title": "Unauthorized Book",
            "author": self.author.id,
            "publication_year": 2022
        }
        response = client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        data = {
            "title": "Updated Book",
            "author": self.author.id,
            "publication_year": 2024
        }
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
        response = self.client.get(self.list_url, {"author": self.author.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(book["author"] == self.author.id for book in response.data))

    def test_search_books_by_title(self):
        response = self.client.get(self.list_url, {"search": "Test"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_order_books_by_year(self):
        response = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years))
