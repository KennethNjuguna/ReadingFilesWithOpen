import numpy as np
import pandas as pd
df= 13495, 16500, 18920, 41315, 5151, 6295
bins=np.linspace(min(df['price'])),max(df['price'])
group_names =['Low','Medium','High']
df['price-binned']=pd.cut(df["price"],bins,labels=group_names,include_lowest=True)