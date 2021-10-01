

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

if s.check_url(url):
    dic=s.read_url(url)

    df=pd.DataFrame(dic)
    print(df)
    df.to_csv("Dog_breed_pandas.txt", header=None, index=None, sep=' ', mode='a')
else:
    print("not exists")