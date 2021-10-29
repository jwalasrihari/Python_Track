from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
import pandas as pd

#Flask
app = Flask(__name__)

#Intially page of website
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about_data')
def about_data():
    return render_template('about_data.html')

@app.route('/data_pre-processing')
def data_cleaning():
    return render_template('data_cleaning.html')

@app.route('/pdf')
def pdf():
    return render_template('pdf.html')

@app.route('/images')
def images():
    return render_template('images.html')




@app.route('/regression_a')
def regression_a():
    return render_template('regression_analysis.html')

@app.route('/anv')
def analyse_n_visulize():
    return render_template('analysis_n_visualization.html')

@app.route('/conclusion')
def conclusion():
    return render_template('conclusion.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)