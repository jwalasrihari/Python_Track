
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
        #getting details of Afghan Hound
        if i['name']=="Afghan Hound":
            print(i['name'],i['breed_group'],i['life_span'],i['temperament'],i['reference_image_id'],sep="\n")
            break
    else:
        print("Afghan hound is not present")
else:
    print("URL not exits")
