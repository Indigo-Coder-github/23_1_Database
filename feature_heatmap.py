import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from category_encoders import OrdinalEncoder
from scipy import stats
from sklearn.preprocessing import LabelBinarizer    

#EmployeeCount랑 EmployeeNumber ㅈ도 의미없는거 같음

df = pd.read_csv('HR Employee Attrition.csv').drop(["EmployeeCount", "EmployeeNumber", "StandardHours", "Over18"], axis=1)
df_Yes = df[df["Attrition"]=="Yes"]
df_No = df[df["Attrition"]=="No"]

continuous_column = ["Age", "DailyRate", "DistanceFromHome", "HourlyRate", "MonthlyIncome", "MonthlyRate",
                     "NumCompaniesWorked", "PercentSalaryHike", "TotalWorkingYears", "TrainingTimesLastYear",
                     "YearsAtCompany", "YearsInCurrentRole", "YearsSinceLastPromotion", "YearsWithCurrManager"]
binary_column = ["Attrition", "Gender", "OverTime", "PerformanceRating"]
category_column = ["BusinessTravel", "Department", "EducationField", "JobRole", "MaritalStatus"]
ordinary_column = ["Education", "EnvironmentSatisfaction", "JobInvolvement", "JobLevel", "JobSatisfaction",
                   "RelationshipSatisfaction", "StockOptionLevel", "WorkLifeBalance"]

##pearson
#df_Yes_pearson = df_Yes[continuous_column].corr("pearson")
#df_No_pearson = df_No[continuous_column].corr("pearson")
#sns.heatmap(df_Yes_pearson[np.abs(df_Yes_pearson) >= 0.1],
#            annot=True, cmap="coolwarm", 
#            linewidths=0.5, linecolor="black",
#            vmin=-1.0, vmax=1.0)
#plt.show()
#sns.heatmap(df_No_pearson[np.abs(df_No_pearson) >= 0.1],
#            annot=True, cmap="coolwarm", 
#            linewidths=0.5,linecolor="black",
#            vmin=-1.0, vmax=1.0)
#plt.show()
#
##kendall-tau
#df_Yes_kendall = df_Yes.corr("kendall")[ordinary_column]
#df_No_kendall = df_No.corr("kendall")[ordinary_column]
#sns.heatmap(data=df_Yes_kendall[np.abs(df_Yes_kendall) >= 0.1],
#            annot=True, cmap="coolwarm", 
#            linewidths=0.5, linecolor="black",
#            vmin=-1.0, vmax=1.0)
#plt.show()
#sns.heatmap(df_No_kendall[np.abs(df_No_kendall) >= 0.1],
#            annot=True, cmap="coolwarm", 
#            linewidths=0.5,linecolor="black",
#            vmin=-1.0, vmax=1.0)
#plt.show()
#
##spearman
#df_Yes_spearman = df_Yes.corr("spearman")[ordinary_column]
#df_No_spearman = df_No.corr("spearman")[ordinary_column]
#sns.heatmap(df_Yes_spearman[np.abs(df_Yes_spearman) >= 0.1],
#            annot=True, cmap="coolwarm", 
#            linewidths=0.5, linecolor="black",
#            vmin=-1.0, vmax=1.0)
#plt.show()
#sns.heatmap(df_No_spearman[np.abs(df_No_spearman) >= 0.1],
#            annot=True, cmap="coolwarm", 
#            linewidths=0.5,linecolor="black",
#            vmin=-1.0, vmax=1.0)
#plt.show()

#point-baserial correlation
df_r_pbr, df_p_pbr = (pd.DataFrame(index=df.drop(binary_column, axis=1).columns,
                                   columns=binary_column).astype(float),
                      pd.DataFrame(index=df.drop(binary_column, axis=1).columns,
                                   columns=binary_column).astype(float))
df[binary_column] = pd.DataFrame(LabelBinarizer().fit_transform(df[binary_column])) 
df = pd.DataFrame(OrdinalEncoder().fit_transform(df))

for i in df.drop(binary_column, axis=1):
    r, p = stats.pointbiserialr(df[i], df[binary_column])
    print(r,p)

plt.subplot(121)
sns.heatmap(df_r_pbr, annot=True, cmap="coolwarm", vmin=-1.0, vmax=1.0)
plt.yticks(ticks=np.array(range(len(df_r_pbr)))+0.5,labels=df_r_pbr.index)
plt.subplot(122)
sns.heatmap(df_p_pbr[np.abs(df_p_pbr) <= 0.05],
            annot=True, cmap="coolwarm",
            vmin=-1.0, vmax=1.0)
plt.yticks(ticks=np.array(range(len(df_p_pbr)))+0.5,labels=df_p_pbr.index)
plt.show()