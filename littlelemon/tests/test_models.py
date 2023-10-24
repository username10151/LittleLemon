from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title='IceCream', price = 80, inventory = 100)
        expected_item = 'IceCream : 80' 

        self.assertEqual(item.get_item(), expected_item)