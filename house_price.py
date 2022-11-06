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

# scatter plot-totalbsmtsf/saleprcie
var='TotalBsmtSF'
data=pd.concat([df_train['SalePrice'], df_train[var]], axis=1)
data.plot.scatter(x=var, y='SalePrice', ylim=(0, 800000))

