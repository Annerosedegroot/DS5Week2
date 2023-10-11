import pandas as pd
import numpy as np
from langdetect import detect


df = pd.read_excel('tweets.xlsx')

df['Language'] = ''
for index, row in df['Tweet'].iteritems():
    taal = detect(row) 
    df.loc[index, 'Language'] = taal

print(df)