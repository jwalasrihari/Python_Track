'''
PROGRAM DESCRIPITON:
	Retirve data from covid_analysis csv file and plot the graphs on the following. 
    1) Graph of Standard Deviation in Total Vaccinations in USA and India in month of January and February 
    2) Graph of fully vaccinated people in India and USA 
    3) Graph of Partially vaccinated people in India and USA
'''
#PROGRAMMED BY : Badam Jwala Sri Hari
#MAIL ID       : jwalasrihari1330@gmail.com
#DATE          : 12-10-2021
#PYTHON VERSION: 3.9.7
#PANDAS VERSION: 1.3.3
#NUMPY VERSION : 1.20.1
#MATPLOTLIB VERSION: 3.3.4
#CAVEATS       : None
#LICENSE       : None


import pandas as pd
import numpy as np
from statistics import mode
from datetime import datetime as dt
import matplotlib.pyplot as plt

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
    count.append(c.most_common()[i][1])
    names_vacccine.append(c.most_common()[i][0])
    

# Getting the india data from the whole data
india_data=pd.DataFrame(df[df['country']=="India"])
# Type conversion to date
india_date= pd.to_datetime(india_data['date'])
india_vaccinated= india_data['people_fully_vaccinated_per_hundred']
india_partial_vaccinated= india_data['people_vaccinated']


# Getting the usa data from the whole data
usa_data=pd.DataFrame(df[df['country']=="United States"])
# Type conversion to date
usa_date= pd.to_datetime(usa_data['date'])
usa_vaccinated= usa_data['people_fully_vaccinated_per_hundred']
usa_partial_vaccinated= usa_data['people_vaccinated']


# Graph for fully vaccinated for india and usa
# To Exponetial to normal values
plt.ticklabel_format(style='plain')
plt.plot(india_date,india_vaccinated,label='fully vaccination india')
plt.plot(usa_date,usa_vaccinated,label='fully vaccination usa')
plt.xlabel("date")
# Rotating X-axis ticks i.e., date by 45 degree
plt.xticks(rotation = 45)
plt.ylabel("vaccinated")
plt.legend()
plt.savefig("fully_vaccinated.png")
plt.show()



# Graph for partial vaccinated for india and usa
plt.ticklabel_format(style='plain')
plt.plot(india_date,india_partial_vaccinated,label='partial vaccination india')
plt.plot(usa_date,usa_partial_vaccinated,label='partial vaccination usa')
plt.xlabel("date")
plt.xticks(rotation = 45)
plt.ylabel("vaccinated")
plt.legend()
plt.savefig("Partial_vaccinated.png")
plt.show()



#standard deviation
print("In India")
month_std_india=dict(india_data.groupby([india_date.dt.strftime('%B'),india_date.dt.strftime('%Y')])['people_vaccinated'].std())
print(month_std_india)
print("In USA")
month_std_usa=dict(usa_data.groupby([usa_date.dt.strftime('%B'),usa_date.dt.strftime('%Y')])['people_vaccinated'].std())


print(month_std_india.keys(),month_std_india.values())
month_date_india=list(map(lambda i:"-".join(list(i)),sorted(list(month_std_india.keys()),key=lambda i:i[0])))
month_date_usa=list(map(lambda i:"-".join(list(i)),sorted(list(month_std_usa.keys()),key=lambda i:i[0])))
print(month_date_india,month_date_usa)
plt.ticklabel_format(style='plain')
# Graph between india and usa monthly wise
plt.plot(month_date_india,month_std_india.values())
plt.plot(month_date_usa,month_std_usa.values())
plt.savefig("standard_deviation_india_vs_usa.png")
plt.show()
print(month_std_usa)




