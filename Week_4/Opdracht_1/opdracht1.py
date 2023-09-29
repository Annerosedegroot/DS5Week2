import pandas as pd
import numpy as np

def clean_data(file):
    df = pd.read_excel(file, skiprows=[0, 1, 2, 3], sheet_name='20000-211000')
    # rename columns
    new_df = df.rename(columns={'HL': '2018', 'HL.1': '2019', 'HL.2': '2020', 'HL.3': '2021', 'HL.4':'2022'})

    # remove duplicates
    new_df.drop_duplicates()

    # delete result rows, fixing structural errors
    new_df.drop(new_df[new_df['Customer Classification (CRM)'] =='Result'].index, inplace=True)
    
    # Check data types
    new_df.dtypes
    
    # missing data
    new_df = new_df.replace('', np.nan)
    
    
    return new_df
excelfile = 'dataProject4.xlsx'
clean_data(excelfile)

