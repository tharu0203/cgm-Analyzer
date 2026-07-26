import pandas as pd
df = pd.read_csv(r"F:\My project\data\HUPA0001P.csv", sep=";")
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
# Feature Analysis
#Checking how heart rate and glucose depends
print(df[["glucose","heart_rate"]].corr())
print(df.corr(numeric_only=True))
print (df[["steps","glucose"]].corr())
print(df[["glucose","steps"]].corr())
print(df[["glucose","basal_rate"]].corr())

#Parse time
df["time"] = pd.to_datetime(df["time"])

#Visualization of data set
#EDA
#How glucose behaves
import matplotlib.pyplot as plt
df["glucose"].hist()
plt.show()