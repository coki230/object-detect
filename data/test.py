import pandas as pd
import numpy as np
import scipy as sp
import factor_analyzer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt



data = pd.read_csv("owid-covid-data.csv")

# print(data.head(0))
# print(data.head())

# d = data.groupby("location")["excess_mortality"].sum()
# print(d)

# sort_data = data.sort_values("total_cases", ascending=False)
# print(sort_data.head()[["iso_code", "continent", "location", "date", "total_cases"]])

# cross_data = data[["location", "iso_code"]]
# pf = pd.crosstab(index=cross_data["location"], columns=cross_data["iso_code"])
# print(pf)

# pi_data = data[["iso_code", "new_cases"]]
# pf = pd.pivot_table(pi_data, index="iso_code", values="new_cases", aggfunc=np.sum)
# print(pf)

# dc = data[["total_deaths", "total_cases", "new_cases", "total_boosters"]].corr()
# print(dc)

# scaler = StandardScaler()
# dn_data = data[["total_deaths", "total_cases", "new_cases", "total_boosters"]].dropna()
# print(dn_data)
# f_data = scaler.fit_transform(dn_data)
# print(f_data)

# dn_data = data[["total_deaths", "total_cases", "new_cases", "total_boosters"]].dropna()
# print(dn_data)
# km = KMeans(n_init=4, n_clusters=4)
# # km.fit(dn_data)
# label = km.fit_predict(dn_data)
# dn_data["label"] = label
# print(dn_data["label"].value_counts())

print(data.head(0))
print(data[["date", "total_cases"]].dropna())
gd = data[["date", "total_cases"]].dropna().groupby(["date"]).sum()
gdf = pd.DataFrame(gd)
print(gd)

plt.plot(gdf.index, gdf[["total_cases"]])
plt.show()