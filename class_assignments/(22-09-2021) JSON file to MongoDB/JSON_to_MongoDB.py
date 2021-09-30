# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 14:57:25 2021

@author: jwala
"""

import json
from pymongo import MongoClient

class One:
    connection = MongoClient("mongodb://localhost:27017")

    def mongo_connection(self):
        if self.connection:
            return True 
        else:
            return False 
    
    def mongodb_list(self):
        if self.mongo_connection() == True:
            return self.connection.list_database_names()

    def db_exists(self, db_name):
        if db_name in self.mongodb_list():
            return True
        else:
            return False 
    
    def create_new_collection(self, db_name, new_collection):
        if self.connection:
            db_name = self.connection[db_name]
            new_collection = db_name[new_collection]
            return new_collection
        else:
            return("error")
    
    # timestand for mongodb 
    def timestamp():
        import datetime as dt 
        return dt.datetime.now()
    
    def insert_data(self,db_name,collection_name,data):
        if self.connection:
            self.connection[db_name][collection_name].insert_one(data)
            return "success"
        else:
            return "error"
    
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
    x=json.load(file)
    for i in x:
        obj.insert_data(db_name,collection_name,i)
    
obj.display(db_name,collection_name)


