import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
from sklearn.metrics import matthews_corrcoef

#EmployeeCount랑 EmployeeNumber ㅈ도 의미없는거 같음

df = pd.read_csv('HR Employee Attrition.csv').drop(["EmployeeCount", "EmployeeNumber", "StandardHours", "Over18"], axis=1)

continuous_column = ["Age", "DailyRate", "DistanceFromHome", "HourlyRate", "MonthlyIncome", "MonthlyRate",
                     "NumCompaniesWorked", "PercentSalaryHike", "TotalWorkingYears", "TrainingTimesLastYear",
                     "YearsAtCompany", "YearsInCurrentRole", "YearsSinceLastPromotion", "YearsWithCurrManager"]

binary_column = ["Attrition", "Gender", "OverTime", "PerformanceRating"]
df[binary_column] = df[binary_column].replace({"Yes":1, "No":0, "Male":1, "Female":0, 3:0, 4:1})

category_column = ["BusinessTravel", "Department", "EducationField", "JobRole", "MaritalStatus"]
df[category_column] = df[category_column].replace({"Non-Travel":0, "Travel_Rarely":1, "Travel_Frequently":2,
                                                   "Research & Development":0, "Sales":1, "Human Resources":2,
                                                   "Life Sciences":0, "Medical":1, "Marketing":2, "Technical Degree":3, "Other":4,
                                                   "Sales Executive":0, "Research Scientist":1, "Laboratory Technician":2, "Manufacturing Director":3, "Healthcare Representative":4,
                                                   "Single":0, "Married":1, "Divorced":2})

ordinary_column = ["Education", "EnvironmentSatisfaction", "JobInvolvement", "JobLevel", "JobSatisfaction",
                   "RelationshipSatisfaction", "StockOptionLevel", "WorkLifeBalance"]

df_Yes = df[df["Attrition"]==1]
df_No = df[df["Attrition"]==0]

#pearson
#continuous-continuous
df_Yes_pearson = df_Yes[continuous_column].corr("pearson")
df_No_pearson = df_No[continuous_column].corr("pearson")
sns.heatmap(df_Yes_pearson[np.abs(df_Yes_pearson) >= 0.1],
            annot=True, cmap="coolwarm", 
            linewidths=0.5, linecolor="black",
            vmin=-1.0, vmax=1.0)
plt.show()
sns.heatmap(df_No_pearson[np.abs(df_No_pearson) >= 0.1],
            annot=True, cmap="coolwarm", 
            linewidths=0.5,linecolor="black",
            vmin=-1.0, vmax=1.0)
plt.show()

#kendall-tau
#ordinary-ordinary
df_Yes_kendall = df_Yes[ordinary_column].corr("kendall")
df_No_kendall = df_No[ordinary_column].corr("kendall")
sns.heatmap(data=df_Yes_kendall[np.abs(df_Yes_kendall) >= 0.1],
            annot=True, cmap="coolwarm", 
            linewidths=0.5, linecolor="black",
            vmin=-1.0, vmax=1.0)
plt.show()
sns.heatmap(df_No_kendall[np.abs(df_No_kendall) >= 0.1],
            annot=True, cmap="coolwarm", 
            linewidths=0.5,linecolor="black",
            vmin=-1.0, vmax=1.0)
plt.show()

#spearman
#ordinary-continous or ordinary
df_Yes_spearman = df_Yes[ordinary_column+continuous_column].corr("spearman")[ordinary_column]
df_No_spearman = df_No[ordinary_column+continuous_column].corr("spearman")[ordinary_column]
sns.heatmap(df_Yes_spearman[np.abs(df_Yes_spearman) >= 0.1],
            annot=True, cmap="coolwarm", 
            linewidths=0.5, linecolor="black",
            vmin=-1.0, vmax=1.0)
plt.show()
sns.heatmap(df_No_spearman[np.abs(df_No_spearman) >= 0.1],
            annot=True, cmap="coolwarm", 
            linewidths=0.5,linecolor="black",
            vmin=-1.0, vmax=1.0)
plt.show()

#point-biserial
#binary-continuous
#Attrition 기준으로 쪼개놓은 거라서 Attrition에 대한 Point-biserial값을 계산할 수 없기 때문에
#Attrition 부분만 df를 가져와서 계산
df_r_pbr, df_p_pbr = (pd.DataFrame(index=continuous_column, columns=binary_column).astype(float),
                      pd.DataFrame(index=continuous_column, columns=binary_column).astype(float))

for i in continuous_column:
    for j in binary_column:
        if j == "Attrition": df_r_pbr.loc[i][j], df_p_pbr.loc[i][j] = stats.pointbiserialr(df[i], df[j])
        else: df_r_pbr.loc[i][j], df_p_pbr.loc[i][j] = stats.pointbiserialr(df_Yes[i], df_Yes[j])

plt.subplot(121)
sns.heatmap(df_r_pbr[df_p_pbr<=0.05], annot=True, cmap="coolwarm", vmin=-1.0, vmax=1.0)
plt.yticks(ticks=np.array(range(len(df_r_pbr)))+0.5,labels=df_r_pbr.index)
plt.subplot(122)
sns.heatmap(df_p_pbr[df_p_pbr<=0.05], annot=True, cmap="coolwarm", vmin=-1.0, vmax=1.0)
plt.yticks(ticks=np.array(range(len(df_p_pbr)))+0.5,labels=df_p_pbr.index)
plt.show()

df_r_pbr, df_p_pbr = (pd.DataFrame(index=df_No.drop(binary_column, axis=1).columns,
                                   columns=binary_column).astype(float),
                      pd.DataFrame(index=df_No.drop(binary_column, axis=1).columns,
                                   columns=binary_column).astype(float))

for i in continuous_column:
    for j in binary_column:
        if j == "Attrition": df_r_pbr.loc[i][j], df_p_pbr.loc[i][j] = stats.pointbiserialr(df[i], df[j])
        else: df_r_pbr.loc[i][j], df_p_pbr.loc[i][j] = stats.pointbiserialr(df_No[i], df_No[j])

plt.subplot(121)
sns.heatmap(df_r_pbr[df_p_pbr<=0.05], annot=True, cmap="coolwarm", vmin=-1.0, vmax=1.0)
plt.yticks(ticks=np.array(range(len(df_r_pbr)))+0.5,labels=df_r_pbr.index)
plt.subplot(122)
sns.heatmap(df_p_pbr[df_p_pbr<=0.05], annot=True, cmap="coolwarm", vmin=-1.0, vmax=1.0)
plt.yticks(ticks=np.array(range(len(df_p_pbr)))+0.5,labels=df_p_pbr.index)
plt.show()

#Phi correlation
#binary-binary
df_Yes_confusion = pd.DataFrame(columns=binary_column, index=binary_column).astype(float)
for i in binary_column:
    for j in binary_column:
        df_Yes_confusion.loc[i][j] = matthews_corrcoef(df_Yes[i], df_Yes[j])
sns.heatmap(df_Yes_confusion, annot=True, cmap="coolwarm", vmin=-1.0, vmax=1.0)
plt.show()

df_No_confusion = pd.DataFrame(columns=binary_column, index=binary_column).astype(float)
for i in binary_column:
    for j in binary_column:
        df_No_confusion.loc[i][j] = matthews_corrcoef(df_No[i], df_No[j])
sns.heatmap(df_No_confusion, annot=True, cmap="coolwarm", vmin=-1.0, vmax=1.0)
plt.show()

#Cramer's V
#category-category
def cramers_corrected_stat(confusion_matrix):
    chi2 = stats.chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum()
    phi2 = chi2/n
    r,k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k-1)*(r-1))/(n-1))
    rcorr = r - ((r-1)**2)/(n-1)
    kcorr = k - ((k-1)**2)/(n-1)
    return np.sqrt(phi2corr / min( (kcorr-1), (rcorr-1)))

df_Yes_CV = pd.DataFrame(index=category_column, columns=category_column).astype(float)
for i in category_column:
    for j in category_column:
        df_Yes_CV.loc[i][j] = cramers_corrected_stat(pd.crosstab(df_Yes[i], df_Yes[j]).to_numpy())
sns.heatmap(df_Yes_CV, annot=True, cmap="coolwarm", vmin=-1.0, vmax=1.0)
plt.show()

df_No_CV = pd.DataFrame(index=category_column, columns=category_column).astype(float)
for i in category_column:
    for j in category_column:
        df_No_CV.loc[i][j] = cramers_corrected_stat(pd.crosstab(df_No[i], df_No[j]).to_numpy())
sns.heatmap(df_No_CV, annot=True, cmap="coolwarm", vmin=-1.0, vmax=1.0)
plt.show()