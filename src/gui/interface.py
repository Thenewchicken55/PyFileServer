from flask import Flask, request, render_template
import os

class FileUploaderGUI:
    def __init__(self, app):
        self.app = app
        self.upload_folder = 'uploads'
        os.makedirs(self.upload_folder, exist_ok=True)
        self.app.config['UPLOAD_FOLDER'] = self.upload_folder

        @self.app.route('/', methods=['GET', 'POST'])
        def upload_file():
            if request.method == 'POST':
                return self.handle_file_upload()
            return self.render_interface()

    def render_interface(self):
        return render_template('upload.html')

    def handle_file_upload(self):
        if 'file' not in request.files:
            return 'No file part', 400
        file = request.files['file']
        if file.filename == '':
            return 'No selected file', 400
        file.save(os.path.join(self.app.config['UPLOAD_FOLDER'], file.filename))
        return 'File uploaded successfully', 200