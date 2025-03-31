from flask import Flask, request, render_template_string, redirect, url_for, send_from_directory, abort
import os

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(os.getcwd(), "files")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Directory Listing</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
            color: #333;
        }
        header {
            background-color: #4CAF50;
            color: white;
            padding: 1rem;
            text-align: center;
        }
        main {
            padding: 2rem;
        }
        form {
            margin-bottom: 1rem;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            background: white;
            margin: 0.5rem 0;
            padding: 1rem;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        a {
            text-decoration: none;
            color: #4CAF50;
            font-weight: bold;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #d32f2f;
        }
    </style>
</head>
<body>
    <header>
        <h1>Directory Listing</h1>
    </header>
    <main>
        <form action="/" method="post" enctype="multipart/form-data">
            <input type="file" name="file">
            <button type="submit">Upload</button>
        </form>
        <ul>
            {% for item in items %}
            <li>
                <a href="{{ url_for('download_file', filename=item) }}">{{ item }}</a>
                <form action="{{ url_for('delete_file', filename=item) }}" method="post" style="display:inline;" onsubmit="return confirm('Are you sure you want to delete this file?');">
                    <button type="submit">Delete</button>
                </form>
            </li>
            {% endfor %}
        </ul>
    </main>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Handle file upload
        if "file" not in request.files:
            return "No file part", 400
        file = request.files["file"]
        if file.filename == "":
            return "No selected file", 400
        file.save(os.path.join(UPLOAD_FOLDER, file.filename))
        return redirect(url_for("index"))

    # List files in the directory
    items = os.listdir(UPLOAD_FOLDER)
    items.sort()
    return render_template_string(HTML_TEMPLATE, items=items)

@app.route("/files/<filename>")
def download_file(filename):
    # Serve the requested file
    try:
        return send_from_directory(UPLOAD_FOLDER, filename)
    except FileNotFoundError:
        abort(404)

@app.route("/files/<filename>", methods=["POST"])
def delete_file(filename):
    # Delete the requested file
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
        return redirect(url_for("index"))
    else:
        abort(404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8079, debug=True)