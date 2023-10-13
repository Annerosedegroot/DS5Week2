# Predicting the quality of wine

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('winequality-red.csv', sep=';')
print(df.dtypes)

plt.boxplot(df['sulphates'])
plt.show()

# outlier van citric acid
# print(max(df['citric acid']))
# MaxCitricAcid = df[df['citric acid'] == 1.0]
# print(MaxCitricAcid)

# outlier total sulfur diocide > 200
MaxTotalSulfurDiocide = df[df['total sulfur dioxide'] >= 200.0]
print(MaxTotalSulfurDiocide)

# outlier sulphates > 1.75
MaxSulphates = df[df['sulphates'] >= 1.75]
print(MaxSulphates)