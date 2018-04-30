from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/')
def index():
    stuff=['guitars','coffee','cats']
    return render_template('index.j2', stuff=stuff)

@app.route('/about')
def about():
    return render_template('about.j2')

@app.route('/css')
def css():
    return render_template('css.j2')

if __name__ == '__main__':
    app.run(debug=True, port=5000)

