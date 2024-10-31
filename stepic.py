#%%
import pandas as pd
from sktime.utils.plotting import plot_series
from scipy.interpolate import lagrange
import numpy as np

df = pd.read_csv("Tesla_empty.csv", sep=',', index_col=['Date'], date_format=lambda col: pd.to_datetime(col, format=('%m/%d/%Y')))
df.sort_index(inplace=True)
mask = df.isna().any(axis=1)
rows_with_null_values = df.loc[mask]
df['Open'].fillna(df['Open'].median())
df['Open'].interpolate(method='pad', limit=1)
df['Open'].interpolate(method='nearest', limit=1)
poly = lagrange(x, y)
int_value_lag = np.polynominal.Polynominal(poly.coef[::-1])(interpolation_point)
df['Open'].fillna(int_value_lag)
# rows_with_null_values
# plot_series(df['Open'])








# %%
