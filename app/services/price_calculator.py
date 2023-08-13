```python
from app.models.filament import Filament
from app.models.pricing import Pricing
from app.models.infill import Infill

class PriceCalculator:
    def __init__(self, filament_type, filament_weight, infill_percentage):
        self.filament = Filament(filament_type, filament_weight)
        self.infill = Infill(infill_percentage)
        self.pricing = Pricing()

    def calculate_filament_cost(self):
        cost_per_gram = self.pricing.get_cost_per_gram(self.filament.type)
        return cost_per_gram * self.filament.weight

    def calculate_filament_sale_price(self):
        sale_price_per_gram = self.pricing.get_sale_price_per_gram(self.filament.type)
        return sale_price_per_gram * self.filament.weight

    def calculate_gross_profit(self):
        cost = self.calculate_filament_cost()
        sale_price = self.calculate_filament_sale_price()
        return sale_price - cost

    def calculate_price(self):
        gross_profit = self.calculate_gross_profit()
        infill_factor = self.infill.get_infill_factor()
        return gross_profit * infill_factor
```