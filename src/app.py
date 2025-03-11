from flask import Flask, request, render_template
import os
from gui.gui import FileUploaderGUI
from network.transfer import FileTransfer

app = Flask(__name__)
file_transfer = FileTransfer()

@app.route('/')
def index():
    gui = FileUploaderGUI()
    return gui.create_interface()

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part', 400
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    file.save(os.path.join('uploads', file.filename))
    file_transfer.send_file(file.filename)
    return 'File uploaded successfully', 200

if __name__ == '__main__':
    os.makedirs('uploads', exist_ok=True)
    app.run(host='0.0.0.0', port=5000)