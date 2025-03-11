from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('gui.html')

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form['textbox']
    print(f"Submitted text: {text}")  # This will log the text to the Python console
    return 'Text submitted successfully', 200

if __name__ == '__main__':
    app.run(debug=True)