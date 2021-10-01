''' PROGRAM :Create a RESTFul API server in Python Flask. To achieve your target
            kindly go through the following process:-

                1) You have to hit the URL https://api.thedogapi.com/v1/breeds into a
                local JSON file into your localhost.

                2) From the JSON file scrap the data of the breed of dog, country of
                origin, bred for which purpose and the image of the dog.

                3) Display the data in a tabular format into a HTML page.

                4) Send the extracted data into a MongoDB database with basic CRUD
                operations associated with it
 '''


#PROGRAMMED BY : Badam Jwala Sri Hari
#MAIL ID       : jwalasrihari1330@gmail.com
#DATE          : 28-09-2021
#PYTHON VERSION: 3.9.7
#FLASK VERSION : 2.0.1
#CAVEATS       : None
#LICENSE       : None

from flask import Flask
from flask import render_template
from flask import request


import json
from pymongo import MongoClient


import requests
import json



# PYTHON REQUESTS & API
def create_json(data,file):
    with open(file, "w") as file:
        return json.dump(data, file,indent=4)

def read_json(file):
    with open(file)as file:
        return json.load(file)

def check_url(url):
    try:
        url = requests.get(url)
        return True
    except:
        return False

def read_url(url):
    url = requests.get(url)
    return url.json()


# Mongo
connection = MongoClient("mongodb://localhost:27017")

def mongo_connection():
    if connection:
        return True
    else:
        return False

def mongodb_list():
   if mongo_connection() == True:
        return connection.list_database_names()

def db_exists( db_name):
    if db_name in mongodb_list():
        return True
    else:
        return False

def create_new_collection(db_name, new_collection):
    if connection:
        db_name = connection[db_name]
        new_collection = db_name[new_collection]
        return new_collection
    else:
        return("error")


# Inserting data into mongodb
def insert_data(db_name,collection_name,data):
    if connection:
        connection[db_name][collection_name].insert_one(data)
        return "success"
    else:
        return "error"

def display(db_name,collection_name):
    a=[]
    if connection:
        for i in connection[db_name][collection_name].find():
            a.append(i)

        for i in a:
            print(i)
            print("-----------------------------------------------")



# Data is extracted from these URL
url = "https://api.thedogapi.com/v1/breeds"


# temp and headings will be used in result.html
temp=[] # temp is to store the list of all extracted elements
headings=["Image","Name","Bred_for","Country"]



# Checking whether URL is exists or not
if check_url(url)==True:

    # Reading data from url and  storing into json
    d=read_url(url)
    file="dog_breed.json"
    create_json(d,file)

    dic=read_json("dog_breed.json")
    # Extracting the name,origin(country), bred_for,image
    for i in dic:
        one={'name':i['name']}

        if 'origin' in i and len(i['origin'])!=0:
            one['origin']=i['origin']
        else:
            one['origin']="-"

        if 'bred_for' in i and len(i['bred_for'])!=0:
            one['bred_for']=i['bred_for']
        else:
            one['bred_for']="-"

        if 'url' in i['image']:
            one['url']=i['image']['url']
        temp.append([one['url'], [one['name'],one['bred_for'],one['origin']] ])




        # Inserting data into mongodb
        insert_data("mongo_python","dog_breed",one)
        
        

app = Flask(__name__)
@app.route('/')
def index():
    # Heading and temp are kept as an arguments render template
    # So,that we can use them in result.html file to display
    return render_template('result.html',headings=headings,temp=temp)

app.run(debug=True, port=5000)

