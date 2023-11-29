# tests.py

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Category, Post

class BlogAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Create a test category
        self.category = Category.objects.create(name='Test Category')

        # Create a test post
        self.post = Post.objects.create(
            category=self.category,
            title='Test Post',
            content='Test Content',
            author=self.user
        )



    def test_get_posts_list(self):
        url = 'http://127.0.0.1:8000/blog/list/'  # Replace with your actual API endpoint
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Assuming only one post is created in the setUp method

    def test_create_post(self):
        url = 'http://127.0.0.1:8000/blog/create/'  # Replace with your actual API endpoint
        data = {
            'category': self.category.id,
            'title': 'New Post',
            'content': 'New Content',
            'author': self.user.id
        }

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)  # Assuming there's one initial post

    # Add more test cases for category and post details, updates, deletions, etc.
