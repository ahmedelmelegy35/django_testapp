# api/tests/test_api.py

from django.test import TestCase
import json

class ItemAPITestCase(TestCase):
    def test_get_items_returns_200(self):
        # Testing GET request for items list
        response = self.client.get('/api/items/')
        self.assertEqual(response.status_code, 200)
    
    def test_create_item(self):
        # Testing POST request to create an item
        data = {"name": "Test Item", "description": "Unit test item"}
        response = self.client.post('/api/items/', data=json.dumps(data), content_type='application/json')
        self.assertIn(response.status_code, (200, 201))
