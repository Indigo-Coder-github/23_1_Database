import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#EmployeeCount랑 EmployeeNumber ㅈ도 의미없는거 같음

df = pd.read_csv('HR Employee Attrition.csv')

sns.histplot(data=df, x=df['Age'], multiple="stack", stat="percent",
             binwidth=1, discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
#19,20살 histogram 정상적으로 출력 안됨
sns.histplot(data=df, x=df['BusinessTravel'], multiple="stack", stat="percent",
             binwidth=1, discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['DailyRate'], multiple="stack", stat="percent",
             bins=15, binwidth=100, binrange=(100,1500), hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['Department'], multiple="stack", stat="percent",
             hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['DistanceFromHome'], multiple="stack", stat="percent",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['Education'], multiple="stack", stat="percent",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['EducationField'], multiple="stack", stat="percent",
             hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['EnvironmentSatisfaction'], multiple="stack", stat="percent",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.xticks(ticks=[1,2,3,4])
plt.show()
sns.histplot(data=df, x=df['Gender'], multiple="stack", stat="percent",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['HourlyRate'], multiple="stack", stat="percent",
             binwidth=5, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['JobInvolvement'], multiple="stack", stat="percent",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.xticks(ticks=[1,2,3,4])
plt.show()
sns.histplot(data=df, x=df['JobLevel'], multiple="stack", stat="percent",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['JobRole'], multiple="stack", stat="percent",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['JobSatisfaction'], multiple="stack", stat="percent",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.xticks(ticks=[1,2,3,4,5])
plt.show()
sns.histplot(data=df, x=df['MaritalStatus'], multiple="stack", stat="percent",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['MonthlyIncome'], multiple="stack", stat="percent",
             binwidth=500, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['MonthlyRate'], multiple="stack", stat="percent",
             binwidth=1000, bins=27, binrange=(2000,27000), hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['NumCompaniesWorked'], multiple="stack", stat="percent",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['OverTime'], multiple="stack", stat="percent",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['PercentSalaryHike'], multiple="stack", stat="percent",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['PerformanceRating'], multiple="stack", stat="percent",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.xticks(ticks=[3,4])
plt.show()
sns.histplot(data=df, x=df['RelationshipSatisfaction'], multiple="stack", stat="percent",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.xticks(ticks=[1,2,3,4])
plt.show()
sns.histplot(data=df, x=df['StockOptionLevel'], multiple="stack", stat="percent",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.xticks(ticks=[0,1,2,3])
plt.show()
sns.histplot(data=df, x=df['TotalWorkingYears'], multiple="stack", stat="percent",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['TrainingTimesLastYear'], multiple="stack", stat="percent",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['WorkLifeBalance'], multiple="stack", stat="percent",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.xticks(ticks=[1,2,3,4])
plt.show()
sns.histplot(data=df, x=df['YearsAtCompany'], multiple="stack", stat="percent",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['YearsInCurrentRole'], multiple="stack", stat="percent",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.xticks(ticks=list(range(0,19)))
plt.show()
sns.histplot(data=df, x=df['YearsSinceLastPromotion'], multiple="stack", stat="percent",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.show()
sns.histplot(data=df, x=df['YearsWithCurrManager'], multiple="stack", stat="percent",
             discrete=True, hue="Attrition",
             palette=sns.color_palette("Set1",2))
plt.xticks(ticks=list(range(0,18)))
plt.show()