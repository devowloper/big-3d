```python
class Filament:
    def __init__(self, filament_type, cost_price, sale_price):
        self.filament_type = filament_type
        self.cost_price = cost_price
        self.sale_price = sale_price

    def get_gross_profit_margin(self):
        return self.sale_price - self.cost_price

    def __str__(self):
        return f"Filament Type: {self.filament_type}, Cost Price: {self.cost_price}, Sale Price: {self.sale_price}"

PLA = Filament("PLA", 20, 30)
PETG = Filament("PETG", 25, 35)
```