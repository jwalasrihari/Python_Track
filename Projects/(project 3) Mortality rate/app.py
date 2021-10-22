from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

#Flask
app = Flask(__name__)

#Intially page of website
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pdf')
def pdf():
    return render_template('pdf.html')

@app.route('/images')
def images():
    return render_template('images.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)