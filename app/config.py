```python
class Config:
    # Filament types
    PLA = 'PLA'
    PETG = 'PETG'
    FILAMENT_TYPES = [PLA, PETG]

    # Filament cost price per weight (in grams)
    FILAMENT_COST_PRICE = {
        PLA: 0.02,  # cost per gram
        PETG: 0.03  # cost per gram
    }

    # Filament sale price per weight (in grams)
    FILAMENT_SALE_PRICE = {
        PLA: 0.04,  # sale price per gram
        PETG: 0.06  # sale price per gram
    }

    # Gross profit margin
    GROSS_PROFIT_MARGIN = 0.2  # 20%

    # Infill percentage
    INFILL_PERCENTAGE = 20  # 20%

    # File upload configurations
    ALLOWED_EXTENSIONS = {'3mf', 'stl'}
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB

    # 3D model viewer configurations
    MODEL_VIEWER_WIDTH = 800  # in pixels
    MODEL_VIEWER_HEIGHT = 600  # in pixels
```