```python
from flask import Blueprint, request, render_template
from app.services.price_calculator import calculatePrice
from app.services.3d_file_processor import process3DFile

quote = Blueprint('quote', __name__)

@quote.route('/quote', methods=['POST'])
def getQuote():
    file = request.files['file']
    filament_type = request.form.get('filament_type')
    infill_percentage = request.form.get('infill_percentage')

    try:
        weight, dimensions = process3DFile(file)
        price = calculatePrice(filament_type, weight, infill_percentage)
        return render_template('quote.html', price=price, dimensions=dimensions, weight=weight)
    except Exception as e:
        return render_template('quote.html', error=str(e)), 400
```