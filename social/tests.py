from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Followers

class UserTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='testpassword')
        self.user2 = User.objects.create_user(username='user2', password='testpassword')

    def test_user_registration(self):
        response = self.client.post('/register/', {
            'username': 'user3',
            'email': 'user3@example.com',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        response = self.client.post('/api-token-auth/', {
            'username': 'user1',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)

    def test_post_creation(self):
        self.client.login(username='user1', password='testpassword')
        response = self.client.post('/posts/', {'content': 'This is a test post'})
        self.assertEqual(response.status_code, 201)

    def test_follow_user(self):
        self.client.login(username='user1', password='testpassword')
        response = self.client.post(f'/follow/{self.user2.username}/')
        self.assertEqual(response.status_code, 201)
