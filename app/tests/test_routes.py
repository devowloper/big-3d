```python
import unittest
from flask import Flask
from app.routes import upload, quote

class TestRoutes(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.client = self.app.test_client()

    def test_uploadFile(self):
        response = self.client.post('/upload', data={'file': (open('test.stl', 'rb'), 'test.stl')})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'fileUploadSuccess')

    def test_uploadFile_failure(self):
        response = self.client.post('/upload', data={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'fileUploadFailure')

    def test_getQuote(self):
        response = self.client.get('/quote', query_string={'filament_type': 'PLA', 'infill_percentage': 20})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'priceCalculationSuccess')

    def test_getQuote_failure(self):
        response = self.client.get('/quote', query_string={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'priceCalculationFailure')

if __name__ == "__main__":
    unittest.main()
```