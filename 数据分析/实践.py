import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.axes as axes

# 展示中文
plt.rcParams['font.sans-serif'] = ['SimHei']

data = pd.read_csv('02.csv')
print(data.head())

