# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 16:21:33 2021

@author: jwala
"""


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
