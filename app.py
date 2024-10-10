from flask import Flask, render_template, request
from poetry_generator import generate_poem

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    theme = request.form['theme']
    style = request.form['style']
    first_line = request.form.get('first_line', '')
    poem = generate_poem(theme, style, first_line)
    return render_template('index.html', poem=poem)

if __name__ == '__main__':
    app.run(debug=True)
