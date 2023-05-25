import numpy as np
import pandas as pd
df=pd.read_csv('https://archive.ics.uci.edu/ml/datasets/automobile')
bins=np.linspace(min(df["price"])),max(df["price'"])
group_names =['Low','Medium','High']
df['price-binned']=pd.cut(df["price"],bins,labels=group_names,include_lowest=True)

