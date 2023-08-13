```python
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from app.config import Config
from app.services.3d_file_processor import process3DFile
from app.services.price_calculator import calculatePrice
from app.services.3d_model_viewer import display3DModel
from app.routes.upload import uploadFile
from app.routes.quote import getQuote

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('get_quote', filename=filename))
    return render_template('upload.html')

@app.route('/quote/<filename>')
def get_quote(filename):
    weight, dimensions = process3DFile(filename)
    price = calculatePrice(weight, dimensions)
    model_view = display3DModel(filename)
    return render_template('quote.html', price=price, model_view=model_view)

if __name__ == '__main__':
    app.run(debug=True)
```