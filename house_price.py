import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm
from sklearn.preprocessing import StandardScaler
from scipy import stats
import warnings

warnings.filterwarnings('ignore')
# %matplotlib inline
# https://www.kaggle.com/code/pmarcelino/comprehensive-data-exploration-with-python
# bring data
df_train=pd.read_csv('House_Price/data/train.csv')

# Check the decoration
df_train.columns

# descriptive statistics summary
df_train['SalePrice'].describe

# get histogram
sns.distplot(df_train['SalePrice'])

# skewness and kurtosis
print("Skewness: %f" % df_train['SalePrice'].skew())
print("Kurtosis: %f" % df_train['SalePrice'].kurt())

# Check relationship with numerical variables
# scatter plot-grlivarea/saleprice
var='GrLivArea'
data=pd.concat([df_train['SalePrice'], df_train[var]], axis=1)
data.plot.scatter(x=var, y='SalePrice', ylim=(0, 800000))
# plt.show()

# scatter plot-totalbsmtsf/saleprcie
var='TotalBsmtSF'
data=pd.concat([df_train['SalePrice'], df_train[var]], axis=1)
data.plot.scatter(x=var, y='SalePrice', ylim=(0, 800000))
# plt.show()

# Check relationship with categorical features
# box plot-overallqual/saleprice
var='OverallQual'
data=pd.concat([df_train['SalePrice'], df_train[var]], axis=1)
f, ax=plt.subplots(figsize=(8,6))
fig=sns.boxplot(x=var, y='SalePrice', data=data)
fig.axis(ymin=0, ymax=800000)
# plt.show()

# box plot-yearbuilt/saleprice
var='YearBuilt'
data=pd.concat([df_train['SalePrice'], df_train[var]], axis=1)
f, ax=plt.subplots(figsize=(16,8))
fig=sns.boxplot(x=var, y='SalePrice', data=data)
fig.axis(ymin=0, ymax=800000)
plt.xticks(rotation=90)
# plt.show()

