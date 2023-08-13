```python
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
from app.services.3d_file_processor import process3DFile

upload = Blueprint('upload', __name__)

ALLOWED_EXTENSIONS = {'stl', '3mf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@upload.route('/upload', methods=['POST'])
def uploadFile():
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file_data = process3DFile(filename)
        if file_data:
            return jsonify({'message': 'fileUploadSuccess', 'data': file_data}), 200
        else:
            return jsonify({'message': 'fileUploadFailure'}), 500
    else:
        return jsonify({'message': 'Invalid file type'}), 400
```