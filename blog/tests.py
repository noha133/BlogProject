# tests.py

from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Category, Post


class BlogAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

        self.category = Category.objects.create(name="Test Category")

        self.post = Post.objects.create(
            category=self.category,
            title="Test Post",
            content="Test Content",
            author=self.user,
        )

    def test_get_posts_list(self):
        url = "/blog/list/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_post(self):
        url = "blog/create/"
        data = {
            "category": self.category.id,
            "title": "New Post",
            "content": "New Content",
            "author": self.user.id,
        }

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 2)
