#PROGRAM       : JSON creation and reading,
#                Checking whether URL is exists or not and Reading data from URL
#PROGRAMMED BY : Badam Jwala Sri Hari
#MAIL ID       : jwalasrihari1330@gmail.com
#DATE          : 20-09-2021
#PYTHON VERSION: 3.9.7
#CAVEATS       : None
#LICENSE       : None

# PYTHON REQUESTS & API

import requests
import json 
data={
      "movie":"robot",
      "badaget":"200cr"
      }

class jwala_json:
      
    # method to creating JSON file and writing data into to it
    def create_json(self, data):
        with open("inserting_data_checking_purpose.json", "w") as file:
            return json.dump(data, file)
      
    # method to read data from json file
    def read_json(self, file):
        with open(file)as file:
            return json.load(file)
    # method to check whether url exists or not
    def check_url(self, url):
        try:
            url = requests.get(url)
            return True
        except:
            return False
    # method to read darta from URLs
    def read_url(self, url):
        url = requests.get(url)
        return url.text



url = "https://randomuser.me/api/"

s = jwala_json()

print(s.read_url(url))
