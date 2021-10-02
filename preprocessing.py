import pandas as pd
import numpy as np

# reading csv file
df = pd.read_csv('amazon_bestsellers.csv', encoding='utf-8')

# ratings column -> eliminate the part post ratings value
df['Book Rating'] = df['Book Rating'].apply(lambda l: l.split()[0])
df['Book Rating'] = pd.to_numeric(df['Book Rating'])


# users_rated column -> eliminate the comma
df['Users Rated'] = df['Users Rated'].str.replace(',','')
df['Users Rated'] = pd.to_numeric(df['Users Rated'], errors='ignore')

# price column -> remove ₹ symbol
df['Book Price'] = df['Book Price'].str.replace('₹','')
df['Book Price'] = df['Book Price'].apply(lambda l: l.split('.')[0])
df['Book Price'] = pd.to_numeric(df['Book Price'])

# replace 0 to NaN
df.replace('0',np.nan,inplace = True)
df.replace(0,np.nan,inplace = True)

# dropping NaN valued rows
df.dropna(inplace = True)

# save df to pickle for further visualizations
df.to_pickle('pickled_df.pkl')