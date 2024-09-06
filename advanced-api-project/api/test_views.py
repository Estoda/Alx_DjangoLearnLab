from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from .models import Book, Author
from django.contrib.auth.models import User

class BookAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(name='Author One')
        self.book = Book.objects.create(
            title='Sample Book', author=self.author, publication_year=2020
        )
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Authenticate the client for each test
        self.client.login(username='testuser', password='testpass')
    
    def test_create_book(self):
        response = self.client.post('/api/books/', {
            'title': 'New Book',
            'author': self.author.id,
            'publication_year': 2021
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=2).title, 'New Book')
    
    def test_update_book(self):
        response = self.client.put(f'/api/books/{self.book.id}/', {
            'title': 'Updated Book',
            'author': self.author.id,
            'publication_year': 2022
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')
    
    def test_delete_book(self):
        response = self.client.delete(f'/api/books/{self.book.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)
    
    def test_filter_books(self):
        response = self.client.get('/api/books/?publication_year=2020')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book.title)

    def test_search_books(self):
        response = self.client.get('/api/books/?search=Sample')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Sample Book')

    def test_order_books(self):
        response = self.client.get('/api/books/?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Sample Book')

    def test_permission_required_for_creation(self):
        self.client.force_authenticate(user=None)
        response = self.client.post('/api/books/', {
            'title': 'Unauthorized Book',
            'author': self.author.id,
            'publication_year': 2021
        })
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)




