```python
import unittest
from app.services import 3d_file_processor

class Test3DFileProcessor(unittest.TestCase):

    def setUp(self):
        self.processor = 3d_file_processor.process3DFile()

    def test_valid_file(self):
        result = self.processor('test.stl')
        self.assertIsNotNone(result)

    def test_invalid_file(self):
        with self.assertRaises(ValueError):
            self.processor('test.txt')

    def test_dimensions(self):
        result = self.processor('test.stl')
        self.assertTrue('dimensions' in result)

    def test_weight(self):
        result = self.processor('test.stl')
        self.assertTrue('weight' in result)

if __name__ == '__main__':
    unittest.main()
```