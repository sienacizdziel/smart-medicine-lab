# from statsmodels.tsa.stattools import adfuller
# import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import StandardScaler

# read in the data
file = pd.ExcelFile('CMP only.xlsx')
df1 = pd.read_excel(file, 'P1')
print(df1)

# scale data
scaler = StandardScaler()
for (col_name, col_data) in df1.iteritems():
    # need to standardize time / date first columns
    # figure out how to use standard scaler for time series data?
    if col_name == 'Metabolic panel':
        continue
    print(col_data.values)
    print(scaler.fit(col_data.values[1:]))


# #plot the original data
# fig, axes=plt.subplot(3,2)
# axes[0, 0].plot(p1.value); axes[0, 0].set_title('Original Series')
# plot_acf(p1.value, ax=axes[0, 1])

# # test for stationary
# result = adfuller(p1.value.dropna())
# print('ADF Statistic: %f' % result[0])
# print('p-value: %f' % result[1])

