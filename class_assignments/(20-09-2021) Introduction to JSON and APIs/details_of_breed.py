#PROGRAM       : Reading data from dog API and displaying breed_group and URL of dog image details
#PROGRAMMED BY : Badam Jwala Sri Hari
#MAIL ID       : jwalasrihari1330@gmail.com
#DATE          : 20-09-2021
#PYTHON VERSION: 3.9.7
#CAVEATS       : None
#LICENSE       : None

import requests
import json 

class jwala_url:
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

s = jwala_url()

#checking whether URL is exists or not
if s.check_url(url)==True:
    dic=s.read_url(url)
    
    #iterating over list of dictionaries
    for i in dic:
        
        #details of breed_group and images
        if 'breed_group' in i:
            print("Breed_group:",i['breed_group'])
            print("image details are:")
            for k,v in i['image'].items():
                print(k,":",v)
            print("--------------------------------------")
else:
    print("URL not exits")
