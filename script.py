import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import numpy as np

etf = pd.read_csv("/home/abhishek/Desktop/major/mutual/ETFs.csv")
mut = pd.read_csv("/home/abhishek/Desktop/major/mutual/Mutual Funds.csv")

mut.head()
mut.shape
etf.shape


