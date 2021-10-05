'''
PROGRAM DESCRIPITON:
	Find out the total vaccinations administered in India and USA from the given CSV file.
    Also find out what is the % rate of US as compared to INdia in vaccine adminstration?
    Consider the total vbaccines adminstred 
'''

# PROGRAMMED BY: BADAM JWALA SRI HARI
# MAIL ID      : jwalasrihari1330@gmail.com
# DATE         : 04-10-2021
# PYTHON VERSION: 3.9.7
# PANDAS VERSION: 1.3.3
# CAVEATS      : None
# LICENSE      : None

import pandas as pd
import numpy as np
from statistics import mode
from datetime import datetime as dt
# data extraction
df = pd.read_csv('./country_vaccinations.csv')

# vaccine combinations being used

from collections import Counter

country_list = df['country'].unique()

vaccine_ava = df['vaccines'].unique()

vaccine_used = []
for i in country_list:
    vaccine_used.append(df[df['country']==i]['vaccines'].mode(0))
vaccine_used = pd.Series(vaccine_used)
vaccine_mode = []
for i in range(0, 102):
    vaccine_mode.append(vaccine_used[i][0])

words_to_count = (word for word in vaccine_mode if word[:1].isupper())

c = Counter(words_to_count)

count = []

names_vacccine = []

for i in range(0,19):
    #print(c.most_common()[i][0],c.most_common()[i][1])
    count.append(c.most_common()[i][1])
    names_vacccine.append(c.most_common()[i][0])

print("Most widely used vaccine # ", mode(vaccine_mode))

print("vaccines used in India # ", df[df['country']=='India']['vaccines'].mode(0)[0])

print("---------------------------------------")
# unvaccinated countries
people_vaccinated = []

for i in country_list:
    people_vaccinated.append(df[df['country']==i]['people_vaccinated'].sum(0))

index_country = []

countries_unvaccinated = []

for i in range(1,102):
    if(people_vaccinated[i]==0):
        index_country.append(i)

for i in index_country:
    countries_unvaccinated.append(country_list[i])

print("countries unvaccinated # ", countries_unvaccinated)
print("---------------------------------------")
#assignment

def month_wise(country):
    country_data=pd.DataFrame(df[df['country']==country])
    lst=[]
    country_data['date']= pd.to_datetime(country_data['date'])
    month_wise_lst=dict(country_data.groupby(country_data['date'].dt.strftime('%B'))['people_vaccinated'].sum())
    return month_wise_lst


def compare_two_countrys(coun1,coun2):
     month={'1':'January','2':'Febrauary','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
     mw_coun1=month_wise(coun1)
     mw_coun2=month_wise(coun2)
     for x,y in mw_coun1.items():
        if x in mw_coun2:
            if mw_coun1[x]>mw_coun2[x]:
                percentage_variying=((mw_coun1[x]-mw_coun2[x])*100)/mw_coun1[x]
                print(coun1," % of vaccinated more than ",coun2," in month",x," is ",percentage_variying)

            else:
                percentage_variying=((mw_coun2[x]-mw_coun1[x])*100)/mw_coun2[x]
                print(coun2," % of vaccinated more than ",coun1," in month",x," is ",percentage_variying)
print(compare_two_countrys("India","United States"))
