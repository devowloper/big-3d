```python
class Infill:
    def __init__(self, percentage=20):
        self.percentage = percentage

    def get_infill_percentage(self):
        return self.percentage

    def set_infill_percentage(self, percentage):
        self.percentage = percentage
```