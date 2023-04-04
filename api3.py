from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return jsonify({'message': 'No image file provided'}), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify({'message': 'No image file selected'}), 400
    if file:
        im_bytes = file.read()
        im_hash = hashlib.md5(im_bytes).hexdigest()
        return jsonify({'md5_hash': im_hash})
    else:
        return jsonify({'message': 'Unable to read image file'}), 400

if __name__ == '__main__':
    app.run()
