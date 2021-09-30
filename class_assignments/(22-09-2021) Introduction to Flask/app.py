#PROGRAM       : Introduction to Flask Framework
#PROGRAMMED BY : Badam Jwala Sri Hari
#MAIL ID       : jwalasrihari1330@gmail.com
#DATE          : 22-09-2021
#PYTHON VERSION: 3.9.7
#FLASK VERSION : 2.0.1
#CAVEATS       : None
#LICENSE       : None

# Importing the required packages
from flask import Flask 
from flask import render_template 
from flask import redirect 
from flask import url_for 

app = Flask(__name__) 

# Starting page of website
@app.route('/')
def index():
    
    # Returns html page which will renders on the website
    return render_template('index.html')


# Uer page
@app.route('/user')
def user():
    return render_template('user.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
