import pandas as pd
import numpy as np
from re import sub
from decimal import Decimal

# config = {
#     "fname": "E:\\python\\excelpp\\files\\HOTELledgecomparision06-30-23.xlsx", # input file name
#     "n_remove":2, # first and last n rows to remove
#     "swap_cols":[2,4,6], # merge columns
#     "swap_rows":[0], # merge rows
#     "drop_row_with_empty_cols":None, # drop rows if a column is empty, assign None to skip
#     "drop_col_with_empty_row":None, # drop columns if row is empty, assign None to skip
#     "remove_repeating_headers":None, # drop rows with repeating header, assign None to skip
#     "output": "output-HOTELledgecomparision06-30-23-3.xlsx", # output file name
#     "split_rows":{1:"\n",2:"$",3:"$",4:"$",}, # split rows and convert currencies, assign None to skip
# }

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


df = pd.read_excel(config["fname"], keep_default_na=False, header=None)

#remove first and last n rows
if config["n_remove"]!=None:
    df.drop(df.head(config["n_remove"]).index, inplace=True )
    df.drop(df.tail(config["n_remove"]).index, inplace=True )



# replace empty space with nan
df.replace("", np.nan, inplace=True)

# remove empty rows and empty columns
df.dropna(how="all", axis=0, inplace=True )
df.dropna(how="all", axis=1, inplace=True )

def check_splits(x,schar="$"):
    if type(x) == str and str(x).count(schar)>1:
        return str(x).split(schar)
    else:
        return x

def check_newlines(x):
    # lambda x:
    if x.find("\n")>=0:
        return [y for y in x.split(schar) if y]
    else:
        return x

def check_currencies(x, schar="$"):
    # (lambda x:[Decimal(sub(r'[^\d.]','',y)) for y in x.split(schar) if y])
    if type(x)==str:
        if str(x).count(schar)>1:
            tx = [y for y in x.split(schar) if y]
            res = []
            for t in tx:
                # print(t)
                try:
                    d = Decimal(sub(r'[^\d.]','',t))
                    if t.find("(") >= 0 or t.find(")") >= 0:
                        d = -d
                    res.append(float(d))
                except:
                    pass
            return res
        else:
            # print(x)
            if x.find("/") >=0: # skip dates
                return x
            try:
                dd = Decimal(sub(r'[^\d.]','',x))
                if x.find("(") >= 0 or x.find(")") >= 0:
                        dd = -dd
                return float(dd)
            except:
                return x
    else:
        return x
# swap column's non empty cells
if config["swap_cols"] != None:
    for sr in config["swap_cols"]:
       print(sr)
       df.iloc[:,sr+1] = df.iloc[:,sr+1].combine_first(df.iloc[:,sr])
    df.drop(columns=df.columns[config["swap_cols"]], inplace=True)

df.reindex()
# swap row's non empty cells
if config["swap_rows"] != None:
    for sr in config["swap_rows"]:
       df.iloc[sr+1] = df.iloc[sr+1].combine_first(df.iloc[sr])
    df.drop(index=df.index[config["swap_rows"]], inplace=True)

# drop empty columns specified
if config["drop_row_with_empty_cols"] != None:
    for eci in config["drop_row_with_empty_cols"]:
        col_index = df.columns[eci]
        df.dropna(subset=[col_index], inplace=True)

# remove rows that are almost empty
if config["drop_col_with_empty_row"] != None:
    df.dropna(axis=1,thresh=config["drop_col_with_empty_row"], inplace=True)

# remove repeating headers
if config["remove_repeating_headers"]!=None:
    df.reindex()
    df.columns = df.iloc[0]
    df = df[df.iloc[:, 0] != df.columns[0]]

# split rows by newline or currency
if config["split_rows"] != None:
    cols = df.columns
    excols = []
    for colindex, schar in config["split_rows"].items():
        df[cols[colindex]].replace(np.nan, "", inplace=True)
        if schar=="$":
            df[cols[colindex]] = df[cols[colindex]].apply(check_currencies)
        else:
            df[cols[colindex]] = df[cols[colindex]].apply(check_newlines)
        excols.append(cols[colindex])

    df = df.explode(excols).reset_index(drop=False)


# save output
if config["output"] != None:

    df.to_excel(config["output"], index=None, header=None)