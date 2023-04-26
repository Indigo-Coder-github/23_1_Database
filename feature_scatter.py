import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

#EmployeeCount랑 EmployeeNumber ㅈ도 의미없는거 같음

df = pd.read_csv('HR Employee Attrition.csv').drop(["EmployeeCount", "EmployeeNumber", "StandardHours"], axis=1)
df_Yes = df[df["Attrition"]=="Yes"]
df_No = df[df["Attrition"]=="No"]

mask_y = np.zeros_like(df_Yes.value_counts(sort=False).unstack().fillna(0), dtype=np.bool)
mask_y[np.tril_indices_from(mask_y, -1)] = True
mask_n = np.zeros_like(df_Yes.value_counts(sort=False).unstack().fillna(0), dtype=np.bool)
mask_n[np.tril_indices_from(mask_n, -1)] = True

#pearson
sns.heatmap(df_Yes.corr("pearson"), annot=True, cmap="coolwarm", square=True, mask=mask_y)
plt.show()
sns.heatmap(df_No.corr("pearson"), annot=True, cmap="coolwarm", square=True, mask=mask_n)
plt.show()

#kendall-tau
sns.heatmap(df_Yes.corr("kendall"), annot=True, cmap="coolwarm", square=True, mask=mask_y)
plt.show()
sns.heatmap(df_No.corr("kendall"), annot=True, cmap="coolwarm", square=True, mask=mask_n)
plt.show()

#spearman
sns.heatmap(df_Yes.corr("spearman"), annot=True, cmap="coolwarm", square=True, mask=mask_y)
plt.show()
sns.heatmap(df_No.corr("spearman"), annot=True, cmap="coolwarm", square=True, mask=mask_n)
plt.show()