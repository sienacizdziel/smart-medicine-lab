import pandas as pd
# from statsmodels.tsa.stattools import adfuller
# import matplotlib.pyplot as plt

# import data
p1 = pd.read_csv('data/P1_CMP_only_2.xlsx', encoding='unicode_escape')
print(p1)

#plot the original data
fig, axes=plt.subplot(3,2)
axes[0, 0].plot(p1.value); axes[0, 0].set_title('Original Series')
plot_acf(p1.value, ax=axes[0, 1])

# test for stationary
result = adfuller(p1.value.dropna())
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])

