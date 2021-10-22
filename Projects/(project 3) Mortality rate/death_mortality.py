import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
import seaborn as sns

data=pd.read_csv("./data_2.csv")
print(data.isnull().sum())
def linear_regression(x,y,category):
    m=((len(x)*sum(x*y))-(sum(x)*sum(y)))/((len(x)*sum(x*x))-sum(x)**2)
    c=(sum(y)-m*sum(x))/len(x)
    print("m and c of",category[0],'Vs',category[1],"is",m,c)

    plt.xlabel(category[0])
    plt.ylabel(category[1])
    plt.title(category[0]+" Vs "+category[1])
    plt.scatter(x,y)
    plt.plot(x,m*x+c,color="red")
    plt.ticklabel_format(style='plain')
    plt.gcf().set_size_inches(8,8)
    #plt.xticks(rotation=90)
    plt.savefig("./static/"+category[0]+" Vs"+ category[1]+".png",format="png")
    plt.show()

def polynomial_regression(x,y,category):
    poly=PolynomialFeatures(degree=3)
    x_poly=poly.fit_transform(x.reshape(-1,1))
    poly_model=LinearRegression()
    poly_model.fit(x_poly,y.reshape(-1,1))
    y_pred=poly_model.predict(x_poly)

    poly=np.poly1d(np.polyfit(x,y,3))
    print("r2_score of ",category[0],'Vs',category[1],"is",r2_score(y,poly(x)))

    plt.scatter(x,y,c='grey')
    plt.xlabel(category[0])
    plt.ylabel(category[1])
    plt.title(category[0]+" Vs "+category[1])
    plt.plot(x,y_pred,c='red')
    plt.ticklabel_format(style='plain')
    plt.gcf().set_size_inches(8,8)
    #plt.xticks(rotation=90)
    plt.savefig("./static/"+"poly_"+category[0]+" Vs"+ category[1]+".png",format="png")
    plt.show()

def multiple_regression(x,y):
    regression_object=linear_model.LinearRegression()
    regression_object.fit(x,y)
    print(regression_object.coef_)




import seaborn as sns
world_data=data[data["Entity"]=="World"]

risk_factors = [i for i in world_data.columns if i not in ['Entity','Year','Code']]

average_deaths = []

for i in risk_factors:
    average_deaths.append(world_data[i].mean())

df1 = pd.DataFrame(list(zip(risk_factors,average_deaths)),columns=['Risk Factor','Avg. Deaths']).sort_values(by='Avg. Deaths',ascending=False)

sns.set(font_scale = 0.9)
plt.figure(figsize=(20,8),dpi=300)
plt.ticklabel_format(style='plain')
sns.barplot(y='Risk Factor',x='Avg. Deaths',data=df1)
plt.title('Avg. Deaths due to Each Factor - WORLD')
plt.xlabel('Avg. Deaths (in. lakhs)')
plt.savefig('./static/Avg. Deaths due to Each Factor - WORLD.png',format='png')
plt.show()

#--------------------Smoking Vs Second hand smoking-------------------------
smoking=world_data['Smoking']
secondhand_smoke=world_data['Secondhand smoke']

polynomial_regression(smoking.values,secondhand_smoke.values,['Smoking','Secondhand_smoke'])

'''
unsafe_water=world_data['Unsafe water source']
alcohol=world_data['Alcohol use']
polynomial_regression(unsafe_water.values,alcohol.values,['x','y'])'''

#--------------------Vitamin A Vs Low bone mineral density--------------------
vitamin_a=world_data['Vitamin A deficiency']
low_bone_mdensity=world_data['Low bone mineral density']
linear_regression(vitamin_a, low_bone_mdensity,['vitamin A','low_bone_mineraldensity'])

#-------------------Alcohol use Vs Iron deficiency----------------------------
alcohol_use=world_data['Alcohol use']
iron_definiency=world_data['Iron deficiency']
polynomial_regression(alcohol_use.values,iron_definiency.values,['Alcohol_use','Iron_deficiency'])


#------------------Diet high in sodium Vs High systolic blood pressure--------------
high_sodium=world_data['Diet high in sodium']
blood_pressure=world_data['High systolic blood pressure']
linear_regression(high_sodium,blood_pressure,['High sodium','Blood pressure'])

#------------------Non-exclusive breastfeeding Vs High fasting plasma glucose----------
non_exclusive_bf=world_data['Non-exclusive breastfeeding']
glucose=world_data['High fasting plasma glucose']
polynomial_regression(non_exclusive_bf.values,glucose.values,['Non-exclusive breastfeeding','Glucose'])


low_physical_activity=world_data['Low physical activity']

#--------------------Low physical activity Vs High fasting plasma glucose--------------
linear_regression(low_physical_activity,glucose,['Low physical activity','Glucose'])


#--------------------Low physical activity Vs High total cholesterol-------------------
world_data['High total cholesterol'] = world_data['High total cholesterol'].fillna(value=world_data['High total cholesterol'].mean())
cholesterol=world_data['High total cholesterol']
polynomial_regression(low_physical_activity.values,cholesterol.values,['Low physical activity','Cholesterol'])


#--------------------Low physical activity Vs High body-mass index---------------------
high_BMI=world_data['High body-mass index']
linear_regression(low_physical_activity,high_BMI,['Low physical activity','High BMI'])

#--------------------Low bone mineral density,Diet low in nuts and seeds Vs Child stunting---
print("Low bone mineral density,Diet low in nuts and seeds Vs Child stunting")
child_stunting=world_data['Child stunting']
low_bone_low_nut=world_data[['Low bone mineral density','Diet low in nuts and seeds']]
multiple_regression(low_bone_low_nut,child_stunting)

#-------------------- blood pressure, glucose Vs smoking-----------------------------------
print("Blood pressure, Glucose Vs Smoking")
bp_glu=world_data[['High systolic blood pressure','High fasting plasma glucose']]
smoking=world_data['Smoking']
multiple_regression(bp_glu,smoking)

#--------------------- blood pressure, glucose vs Diet low in nuts and seeds---------------
print("blood pressure, glucose vs Diet low in nuts and seeds")
low_nut=world_data['Diet low in nuts and seeds']
multiple_regression(bp_glu,low_nut)

#----------------------unsafe water source, no access to handwashing facility Vs unsafe sanitation--
print("unsafe water source, no access to handwashing facility Vs unsafe sanitation")
water_resou_handwash=world_data[['Unsafe water source','No access to handwashing facility']]
unsafe_sanitation=world_data['Unsafe sanitation']
multiple_regression(water_resou_handwash,unsafe_sanitation)

#---------------------household air pollution from solid fuels, outdoor air pollution Vs air pollution-----
print("household air pollution from solid fuels, outdoor air pollution Vs air pollution")
house_outdoor=world_data[['Household air pollution from solid fuels','Outdoor air pollution']]
pollution=world_data['Air pollution']
multiple_regression(house_outdoor,pollution)