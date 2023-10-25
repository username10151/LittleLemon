from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import menuSerializer
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User  # Import the User model
from rest_framework.authtoken.models import Token  # Import Token mode

class MenuViewTest(TestCase):
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser2', password='testpassword2')

        # Create an authentication token for the user
        self.token = Token.objects.create(user=self.user)
        # Create test instances of the Menu model
        self.menu_item1 = Menu.objects.create(title='Item 1', price=10.0, inventory=100)
        self.menu_item2 = Menu.objects.create(title='Item 2', price=15.0, inventory=50)

    def test_getall(self):
        # Create an API client for making requests
        client = APIClient()

        # Send a GET request to your view
        client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')
        response = client.get(reverse('menu-items-view'))

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Serialize the menu items
        serialized_data = menuSerializer([self.menu_item1, self.menu_item2], many=True).data

        # Check if the response data matches the serialized data
        self.assertEqual(response.data, serialized_data)