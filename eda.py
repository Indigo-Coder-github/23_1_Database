import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns

#EmployeeCount랑 EmployeeNumber ㅈ도 의미없는거 같음

df = pd.read_csv('HR Employee Attrition.csv')
#sns.histplot(data=df['Age'], bins=len(df['Age'].unique()), discrete=True)
#plt.show()
#sns.histplot(df['Attrition'])
#plt.show()
#sns.histplot(df['BusinessTravel'])
#plt.show()
#sns.histplot(df['DailyRate'], bins=15, binwidth=100, binrange=(100,1500))
#plt.show()
#sns.histplot(df['Department'])
#plt.show()
#sns.histplot(df['DistanceFromHome'], discrete=True)
#plt.show()
#sns.histplot(df['Education'], discrete=True)
#plt.show()
#sns.histplot(df['EducationField'])
#plt.show()
#sns.histplot(df['EnvironmentSatisfaction'], discrete=True)
#plt.xticks(ticks=[1,2,3,4])
#plt.show()
#sns.histplot(df['Gender'])
#plt.show()
#sns.histplot(df['HourlyRate'], bins=16, binwidth=5, binrange=(30,100))
#plt.show()
#sns.histplot(df['EnvironmentSatisfaction'], discrete=True)
#plt.xticks(ticks=[1,2,3,4])
#plt.show()
#sns.histplot(df['JobLevel'], discrete=True)
#plt.show()
#sns.histplot(df['JobRole'])
#plt.show()