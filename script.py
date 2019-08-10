import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

%matplotlib inline

plt.style.use("classic")

etf = pd.read_csv("/home/abhishek/Desktop/major/mutual/ETFs.csv")
mut = pd.read_csv("/home/abhishek/Desktop/major/mutual/Mutual Funds.csv")

# mut.head()
# mut.shape
# etf.shape

plot = plt.matshow(etf.corr())
plt.show()
plot.savefig("Correlation")

# Correlation matrix
etf_corr = etf.corr()
mut_corr = mut.corr()

# Writting the correlation matrix to a csv
etf_corr.to_csv(r"/home/abhishek/Desktop/major/Portfolio-Optimisation/mutual/etf_correlation.csv")
mut_corr.to_csv(r"mutual/mut_correlation.csv")


cor = mut.corr()
sns.heatmap(cor,robust=True,annot=True)
# sns.pairplot(cor)