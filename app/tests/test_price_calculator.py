```python
import unittest
from app.services.price_calculator import calculatePrice
from app.models.filament import Filament
from app.models.pricing import Pricing
from app.models.infill import Infill

class TestPriceCalculator(unittest.TestCase):

    def setUp(self):
        self.filament = Filament('PLA', 1.24)  # weight in kg
        self.pricing = Pricing(20, 25, 20)  # cost price, sale price, profit margin in %
        self.infill = Infill(20)  # infill percentage

    def test_calculatePrice(self):
        price = calculatePrice(self.filament, self.pricing, self.infill)
        self.assertIsNotNone(price)
        self.assertGreater(price, 0)

    def test_calculatePrice_with_invalid_filament(self):
        with self.assertRaises(ValueError):
            calculatePrice(None, self.pricing, self.infill)

    def test_calculatePrice_with_invalid_pricing(self):
        with self.assertRaises(ValueError):
            calculatePrice(self.filament, None, self.infill)

    def test_calculatePrice_with_invalid_infill(self):
        with self.assertRaises(ValueError):
            calculatePrice(self.filament, self.pricing, None)

if __name__ == '__main__':
    unittest.main()
```