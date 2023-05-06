import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('HR Employee Attrition.csv').drop(["EmployeeCount", "EmployeeNumber", "StandardHours", "Over18"], axis=1)

plt.show()