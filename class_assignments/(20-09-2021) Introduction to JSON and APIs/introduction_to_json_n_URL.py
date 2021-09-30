# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 15:57:38 2021

@author: jwala
"""

# PYTHON REQUESTS & API

import requests
import json 
data={
      "movie":"robot",
      "badaget":"200cr"
      }

class jwala_json:
    def create_json(self, data):
        with open("inserting_data_checking_purpose.json", "w") as file:
            return json.dump(data, file)
    
    def read_json(self, file):
        with open(file)as file:
            return json.load(file)
    
    def check_url(self, url):
        try:
            url = requests.get(url)
            return True
        except:
            return False

    def read_url(self, url):
        url = requests.get(url)
        return url.text



url = "https://randomuser.me/api/"

s = jwala_json()

print(s.read_url(url))
