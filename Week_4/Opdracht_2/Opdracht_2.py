import pandas as pd
import numpy as np

df = pd.read_excel('hotelBookings.xlsx')

# in kolom stays_in_week_nights is een 4.3
df['stays_in_weekend_nights'] = df['stays_in_weekend_nights'].replace([4.3], 4)


# kolom lead_time is een outlier 737, de rest is tussen 0 en 400



# country heeft een 2 en 3 en NULL

# Filter de rijen waar de waarde in de kolom 'country' gelijk is aan '2', '3' of 'NULL'
df.dropna(subset = ['country'], inplace=True)
condition = (df['country'] == 2) | (df['country'] == 3)

# Droppen van de geselecteerde rijen met behulp van de 'drop' functie
df = df.drop(df[condition].index)

# Reset de index van het DataFrame na het droppen van de rijen
df = df.reset_index(drop=True)

# country lay out sommige spaties
df['country'] = df['country'].str.replace(' ', '')


# arrival_date_year is een jaar 2099
df['arrival_date_year'] = df['arrival_date_year'].replace(2099, 2015)


# arrival_date_month zijn er blanks
check_nan = df['arrival_date_month'].isnull().values.any()
    

# meal heeft spaties voor sommige waarden
df['meal'] = df['meal'].str.replace(' ', '')


# adults iemand heeft 3500 personene
mean = (sum(df['adults'])-3500) / len(df['adults'])
afgerond = round(mean)
df['adults'] = df['adults'].replace(3500, afgerond)

# children heeft 200 en 55000 kinderen
gemiddelde = (df[df['adults']==2]['children']).mean()
print(gemiddelde)

# rij waardes agent en company zijn omgewisseld: 223, 224, 225, 300, 392, 455, 546, 605, 633, 801, 942
