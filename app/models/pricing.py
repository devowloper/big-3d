```python
class Pricing:
    def __init__(self, filament_type, cost_price, sale_price, gross_profit_margin):
        self.filament_type = filament_type
        self.cost_price = cost_price
        self.sale_price = sale_price
        self.gross_profit_margin = gross_profit_margin

    def calculate_profit(self):
        return self.sale_price - self.cost_price

    def calculate_margin(self):
        return (self.calculate_profit() / self.sale_price) * 100

    def is_profitable(self):
        return self.calculate_margin() >= self.gross_profit_margin
```