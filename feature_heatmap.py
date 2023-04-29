import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
from sklearn.preprocessing import LabelBinarizer
from category_encoders import OrdinalEncoder

#EmployeeCount랑 EmployeeNumber ㅈ도 의미없는거 같음

df = pd.read_csv('HR Employee Attrition.csv').drop(["EmployeeCount", "EmployeeNumber", "StandardHours", "Over18"], axis=1)
df_Yes = df[df["Attrition"]=="Yes"]
df_No = df[df["Attrition"]=="No"]

mask = np.zeros([23,23], dtype=np.bool)
mask[np.tril_indices_from(mask, -1)] = True

#pearson
df_Yes_pearson = df_Yes.corr("pearson")
df_No_pearson = df_No.corr("pearson")
sns.heatmap(df_Yes_pearson[np.abs(df_Yes_pearson) >= 0.1],
            annot=True, cmap="coolwarm", mask=mask,
            linewidths=0.5, linecolor="black")
plt.show()
sns.heatmap(df_No_pearson[np.abs(df_No_pearson) >= 0.1],
            annot=True, cmap="coolwarm", mask=mask,
            linewidths=0.5,linecolor="black")
plt.show()

#kendall-tau
df_Yes_kendall = df_Yes.corr("kendall")
df_No_kendall = df_No.corr("kendall")
sns.heatmap(df_Yes_pearson[np.abs(df_Yes_kendall) >= 0.1],
            annot=True, cmap="coolwarm", mask=mask,
            linewidths=0.5, linecolor="black")
plt.show()
sns.heatmap(df_No_pearson[np.abs(df_No_kendall) >= 0.1],
            annot=True, cmap="coolwarm", mask=mask,
            linewidths=0.5,linecolor="black")
plt.show()

#spearman
df_Yes_spearman = df_Yes.corr("spearman")
df_No_spearman = df_No.corr("spearman")
sns.heatmap(df_Yes_pearson[np.abs(df_Yes_spearman) >= 0.1],
            annot=True, cmap="coolwarm", mask=mask,
            linewidths=0.5, linecolor="black")
plt.show()
sns.heatmap(df_No_pearson[np.abs(df_No_spearman) >= 0.1],
            annot=True, cmap="coolwarm", mask=mask,
            linewidths=0.5,linecolor="black")
plt.show()

#point-baserial correlation
df_r_pbr, df_p_pbr = (pd.DataFrame(index=df.drop(["Attrition", "Gender", "OverTime", "PerformanceRating"], axis=1).columns,
                                   columns=["Attrition", "Gender", "OverTime", "PerformanceRating"]).astype(float),
                      pd.DataFrame(index=df.drop(["Attrition", "Gender", "OverTime", "PerformanceRating"], axis=1).columns,
                                   columns=["Attrition", "Gender", "OverTime", "PerformanceRating"]).astype(float))
df["Attrition"] = pd.DataFrame(LabelBinarizer().fit_transform(df["Attrition"]))
df["Gender"]  = pd.DataFrame(LabelBinarizer().fit_transform(df["Gender"]))
df["OverTime"] = pd.DataFrame(LabelBinarizer().fit_transform(df["OverTime"]))
df["PerformanceRating"] = pd.DataFrame(LabelBinarizer().fit_transform(df["PerformanceRating"]))
df = pd.DataFrame(OrdinalEncoder().fit_transform(df))

for i in df.drop(["Attrition", "Gender", "OverTime", "PerformanceRating"], axis=1):
    r, p = stats.pointbiserialr(df[i], df["Attrition"])
    df_r_pbr["Attrition"][i] = r
    df_p_pbr["Attrition"][i] = p
    
    r, p = stats.pointbiserialr(df[i], df["Gender"])
    df_r_pbr["Gender"][i] = r
    df_p_pbr["Gender"][i] = p
    
    r, p = stats.pointbiserialr(df[i], df["OverTime"])
    df_r_pbr["OverTime"][i] = r
    df_p_pbr["OverTime"][i] = p
    
    r, p = stats.pointbiserialr(df[i], df["PerformanceRating"])
    df_r_pbr["PerformanceRating"][i] = r
    df_p_pbr["PerformanceRating"][i] = p

plt.subplot(121)
sns.heatmap(df_r_pbr, annot=True, cmap="coolwarm")
plt.yticks(ticks=np.array(range(len(df_r_pbr)))+0.5,labels=df_r_pbr.index)
plt.subplot(122)
sns.heatmap(df_p_pbr[np.abs(df_p_pbr) <= 0.05],
            annot=True, cmap="coolwarm")
plt.yticks(ticks=np.array(range(len(df_p_pbr)))+0.5,labels=df_p_pbr.index)
plt.show()