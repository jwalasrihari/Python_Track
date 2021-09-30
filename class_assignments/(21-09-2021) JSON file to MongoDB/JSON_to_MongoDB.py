#PROGRAM       : JSON file data should be inserted into MongoDB
#                and some operations to interact with mongoDB
#PROGRAMMED BY : Badam Jwala Sri Hari
#MAIL ID       : jwalasrihari1330@gmail.com
#DATE          : 21-09-2021
#PYTHON VERSION: 3.9.7
#CAVEATS       : None
#LICENSE       : None

import json
from pymongo import MongoClient

class One:
    
    #Estabilshing the connect with MongoDB
    connection = MongoClient("mongodb://localhost:27017")
    
    # Method returns TRUE if connection is established else it will return FALSE
    def mongo_connection(self):
        if self.connection:
            return True 
        else:
            return False 
    
    # Method gives list of databased 
    def mongodb_list(self):
        if self.mongo_connection() == True:
            return self.connection.list_database_names()
        
    # Method checks whether db exists or not
    def db_exists(self, db_name):
        if db_name in self.mongodb_list():
            return True
        else:
            return False 
        
    # Method to create new collection in a particular database
    def create_new_collection(self, db_name, new_collection):
        if self.connection:
            db_name = self.connection[db_name]
            new_collection = db_name[new_collection]
            return new_collection
        else:
            return("error")
    
    # timestamp for mongodb 
    def timestamp():
        import datetime as dt 
        return dt.datetime.now()
    
    #method inserting single document into a particular collection and database
    def insert_data(self,db_name,collection_name,data):
        if self.connection:
            self.connection[db_name][collection_name].insert_one(data)
            return "success"
        else:
            return "error"
    
    #method to display data in particular collection
    def display(self,db_name,collection_name):
        a=[]
        if self.connection:
            for i in self.connection[db_name][collection_name].find():
                a.append(i)
               
            for i in a:
                print(i)
                print("-----------------------------------------------")

    
obj=One()

db_name="mongo_python"
collection_name="product"

print(obj.db_exists(db_name))
print(obj.create_new_collection(db_name,collection_name))
file="product.json"
with open(file)as file:
    
    # Loading the data from json file 
    # x is list of documents
    x=json.load(file)
    
    # Iterating over the list of documents and calling the insert_data method 
    for i in x:
        obj.insert_data(db_name,collection_name,i)
    
# Display the all the documents 
# To verifying whether documents inserted or not
obj.display(db_name,collection_name)


