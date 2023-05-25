import numpy as np
import pandas as pd
import matplotlib as plt
df= pd.read_csv('Automobile_data.csv')
bins=np.linspace(min(df["price"])),max(df["price'"])
group_names =['Low','Medium','High']
df['price-binned']=pd.cut(df["price"],bins,labels=group_names,include_lowest=True)

df['price-binned']
plt.title['price bins']
plt.xtitle['price']
plt.ytitle['count']


