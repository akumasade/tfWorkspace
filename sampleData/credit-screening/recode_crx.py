# Script clean/encode credit card data
import numpy as np
import pandas as pd

raw = pd.read_table("./crx.data", delimiter=",", header=None)

columns = ['A16', 'A1','A2', 'A3', 'A8', 'A9', 'A10', 'A11',\
        'A12', 'A14', 'A15']
index = range(len(raw))

new = pd.DataFrame(index=index, columns=columns)

#replace missing data with -1
data = raw.replace("?", -1)

# recode A1
new['A1'] = data[0].replace("a", 0)
new['A1'] = new['A1'].replace("b", 1)

# recode A16
new['A16'] = data[15].replace("+", 1)
new['A16'] = new['A16'].replace("-", 0)

# recode A9, A10, A12
inds = [8, 9, 11]
new_ind = ['A9', 'A10', 'A12']
new[new_ind] = data[inds].replace("t", 1)
new[new_ind] = new[new_ind].replace("f", 0)

# Continuous data
inds = [1, 2, 7, 10, 13, 14]
new_ind = ['A2', 'A3', 'A8', 'A11', 'A14', 'A15']
new[new_ind] = data[inds]

# hash trick for A4 A5 A6 A7 A13
# taken from https://stackoverflow.com/questions/8673035/what-is-feature-hashing-hashing-trick
hash_ind = [3, 4, 5, 6, 12]
temp = data[hash_ind]
hashed_cols = []
def hash_col(df, col, N):
    cols = ["A"+str(col+1)+ "_" + str(i) for i in range(N)]
    out_data = pd.DataFrame(index=range(len(df)), columns=cols)
    def xform(x): tmp = [0 for i in range(N)]; tmp[hash(x) % N] = 1; return pd.Series(tmp,index=cols)
    out_data[cols] = df[col].apply(xform)
    return out_data

for name in temp.columns.values :
    lel = hash_col(temp, name, 3)
    new = pd.concat([new, lel], axis=1)

#save it
new.to_csv("./crx-recoded.csv", index=False)
