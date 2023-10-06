import pandas as pd
import numpy as np

df = pd.read_excel('hotelBookings.xlsx')

# in kolom stays_in_week_nights is een 4.3
df['stays_in_weekend_nights'] = df['stays_in_weekend_nights'].replace([4.3], 4)

    

# kolom lead_time is een outlier 737, de rest is tussen 0 en 400

# country heeft een 2 en 3 en NULL
# if df['country'] == '2' or '3' or 'NULL':
#     df.drop()

# country lay out sommige spaties

# arrival_date_year is een jaar 2099

# arrival_date_month zijn er blanks

# meal heeft spaties voor sommige waarden

# adults iemand heeft 3500 personene

# children heeft 200 en 55000 kinderen

# rij waardes agent en company zijn omgewisseld: 223, 224, 225, 300, 392, 455, 546, 605, 633, 801, 942