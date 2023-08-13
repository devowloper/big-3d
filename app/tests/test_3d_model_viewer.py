```python
import unittest
from app.services.3d_model_viewer import display3DModel

class Test3DModelViewer(unittest.TestCase):

    def setUp(self):
        self.valid_3mf_file = 'test_files/valid.3mf'
        self.valid_stl_file = 'test_files/valid.stl'
        self.invalid_file = 'test_files/invalid.txt'

    def test_display3DModel_valid_3mf(self):
        result = display3DModel(self.valid_3mf_file)
        self.assertTrue(result)

    def test_display3DModel_valid_stl(self):
        result = display3DModel(self.valid_stl_file)
        self.assertTrue(result)

    def test_display3DModel_invalid_file(self):
        with self.assertRaises(Exception):
            display3DModel(self.invalid_file)

if __name__ == '__main__':
    unittest.main()
```