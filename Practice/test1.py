import pandas as pd
import matplotlib
import numpy as np
config = {
    "fname": "D:\\pythondemo\\files\\HOTELledgecomparision06-30-23 (1).xlsx", # input file name, mandatory cannot skip
    "n_remove":1, # first and last n rows to remove, assign None to skip
    "swap_cols":None, # merge columns, assign None to skip
    "swap_rows":[0], # merge rows, assign None to skip
    "drop_row_with_empty_cols":[0,-1], # drop rows if a column is empty, assign None to skip
    "drop_col_with_empty_row":15, # drop columns if row is empty, assign None to skip
    "remove_repeating_headers":True,  # drop rows with repeating header, assign None to skip
    "output": "output-HOTELledgecomparision06-30-23 (1).xlsx", # output file name, assign None to skip
    "split_rows":{-1:"$"}, #last column is -1, second last column is -2 and vice versa
}
d=pd.read_excel("C:\\Users\\anand.adapa\\Downloads\\HOTELledgecomparision06-30-23.xlsx",keep_default_na=False,header=None)
df=pd.DataFrame(d)
#df.replace("hii",np.nan)
df.dropna(axis=1,how="all")
df.dropna(axis=0,how="all")
def check_splits(x,schar="$"):
    if type(x) == str and str(x).count(schar)>1:
        return str(x).split(schar)
    else:
        return x



df.to_excel("C:\\Users\\anand.adapa\\Downloads\\NEWHOTELledgecomparision06-30-23.xlsx")



print(df.to_string())      
