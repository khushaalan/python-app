from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/redirect')
def redirect_to_about():
    return redirect(url_for('about'))

if __name__ == '__main__':
    app.run()
