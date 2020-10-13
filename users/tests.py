from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='test',password='test')
        user.save()

    def test_jwt_authentication(self):
        response = self.client.post('/api/token/',{'username':'test','password':'test'})
        self.assertEqual(response.status_code, 200)