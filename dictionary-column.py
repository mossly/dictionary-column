import pandas as pd
import numpy as np

def newColumnFromDictionary(df, keyColumn, valueColumn, keys, values):
	keys = [df[keyColumn].str.contains(k) == True for c in keys]

	df[valueColumn] = np.select(keys, values)

	return df

keys = pd.read_csv("dictionary.csv")['Key'].values.tolist()
values = pd.read_csv("dictionary.csv")['Value'].values.tolist()

df = pd.read_csv("input.csv")

df = newColumnFromDictionary(df, 'newCol', 'refCol', keys, values)

df.to_csv("input.csv", index=False)
