from flask import Flask, render_template
app = Flask(__name__)

pages = ['index', 'about'];

@app.route('/')
def index():
    return render_template('index.j2', pages=pages )

@app.route('/about')
def about():
    return render_template('about.j2', pages=pages)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

