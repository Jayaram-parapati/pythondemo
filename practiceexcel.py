import pandas as pd
import numpy as np
from re import sub
from decimal import Decimal

d = pd.read_excel("D:\\pythondemo\\files\\HOTELledgecomparision06-30-23 (1).xlsx")
# print(d)
df = pd.DataFrame(d)
df.dropna(axis=0 , how= "all", inplace=True)
df.dropna(axis=1 , how= "all", inplace=True)
df.drop(df.head(2).index, inplace=True )
print(df.head(2).index)
df.drop(df.tail(2).index, inplace=True )
# df.replace("hii", np.nan, inplace=True)

# if 0 != None:
#     for sr in [0]:
#        df.iloc[sr+1] = df.iloc[sr+1].combine_first(df.iloc[sr])
#     df.drop(index=df.index[0], inplace=True)

# print(df.to_string())
df.to_excel("D:\\pythondemo\\files\\practiceoutput.xlsx", index=None, header=None)