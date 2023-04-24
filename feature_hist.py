import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import seaborn as sns

#EmployeeCount랑 EmployeeNumber ㅈ도 의미없는거 같음

df = pd.read_csv('HR Employee Attrition.csv')

#sns.histplot(data=df, x=df['Age'],
#             binwidth=1, discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.show()
#19,20살 histogram 정상적으로 출력 안됨
#sns.histplot(data=df, x=df['BusinessTravel'],
#             binwidth=1, discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.show()
#sns.histplot(data=df, x=df['DailyRate'],
#             bins=15, binwidth=100, binrange=(100,1500), hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.show()
#sns.histplot(data=df, x=df['Department'],
#             hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.show()
#sns.histplot(data=df, x=df['DistanceFromHome'],
#             discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.show()
#sns.histplot(data=df, x=df['Education'],
#             discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.show()
#sns.histplot(data=df, x=df['EducationField'],
#             hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.show()
#sns.histplot(data=df, x=df['EnvironmentSatisfaction'],
#             discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.xticks(ticks=[1,2,3,4])
#plt.show()
#sns.histplot(data=df, x=df['Gender'],
#             discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.show()
#sns.histplot(data=df, x=df['HourlyRate'],
#             binwidth=5, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.show()
#sns.histplot(data=df, x=df['JobInvolvement'],
#             discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.xticks(ticks=[1,2,3,4])
#plt.show()
#sns.histplot(data=df, x=df['JobLevel'],
#             discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.show()
#sns.histplot(data=df, x=df['JobRole'],
#             discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.show()
#sns.histplot(data=df, x=df['JobLevel'],
#             discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.xticks(ticks=[1,2,3,4,5])
#plt.show()
#sns.histplot(data=df, x=df['MaritalStatus'],
#             discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.show()
#sns.histplot(data=df, x=df['MonthlyIncome'],
#             binwidth=500, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.show()
#sns.histplot(data=df, x=df['MonthlyRate'],
#             binwidth=1000, bins=27, binrange=(2000,27000), hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.show()
#sns.histplot(data=df, x=df['NumCompaniesWorked'],
#             discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.show()
#sns.histplot(data=df, x=df['OverTime'],
#             discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.show()
#sns.histplot(data=df, x=df['PercentSalaryHike'],
#             discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.show()
#sns.histplot(data=df, x=df['PerformanceRating'],
#             discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.xticks(ticks=[3,4])
#plt.show()
#sns.histplot(data=df, x=df['RelationshipSatisfaction'],
#             discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.xticks(ticks=[1,2,3,4])
#plt.show()
#sns.histplot(data=df, x=df['StockOptionLevel'],
#             discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.xticks(ticks=[0,1,2,3])
#plt.show()
#sns.histplot(data=df, x=df['TotalWorkingYears'],
#             discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.show()
#sns.histplot(data=df, x=df['TrainingTimesLastYear'],
#             discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.show()
#sns.histplot(data=df, x=df['WorkLifeBalance'],
#             discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.xticks(ticks=[1,2,3,4])
#plt.show()
#sns.histplot(data=df, x=df['YearsAtCompany'],
#             discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.show()
#sns.histplot(data=df, x=df['YearsInCurrentRole'],
#             discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.xticks(ticks=list(range(0,19)))
#plt.show()
#sns.histplot(data=df, x=df['YearsSinceLastPromotion'],
#             discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.show()
#sns.histplot(data=df, x=df['YearsWithCurrManager'],
#             discrete=True, hue="Attrition",
#             palette=sns.color_palette("Set1",2))
#plt.xticks(ticks=list(range(0,18)))
#plt.show()