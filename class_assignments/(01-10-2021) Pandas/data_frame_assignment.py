#PROGRAM       : Read data from URL, make dataframe and store the data in txt file
#PROGRAMMED BY : Badam Jwala Sri Hari
#MAIL ID       : jwalasrihari1330@gmail.com
#DATE          : 01-10-2021
#PYTHON VERSION: 3.9.7
#PANDAS VERSION: 1.3.3
#CAVEATS       : None
#LICENSE       : None

# PYTHON REQUESTS & API

import requests
import json
import pandas as pd
import numpy as np

class jwala:
    def create_json(self, data):
        with open("random_user.json", "w") as file:
            return json.dump(data, file,indent=4)

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
        return url.json()



url = "https://api.thedogapi.com/v1/breeds"

s = jwala()


#checking whether the URL is working or not 
if s.check_url(url):
    
    # Reading data from URL 
    dic=s.read_url(url)
    
    # Converting data into dataFrame
    df=pd.DataFrame(dic)
    print(df)
    
    # Storing dataFrame in txt file
    df.to_csv("Dog_breed_pandas.txt", header=None, index=None, sep=' ', mode='a')
else:
    print("not exists")
