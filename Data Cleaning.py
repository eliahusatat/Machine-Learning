import matplotlib
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.show()
import numpy as np
pd.set_option('display.max_columns', None)


df = pd.read_csv('fake_job_postings.csv')


#print(df.head())

print(df.shape)


df2 = df.copy()

df2.nunique()

df.isna().sum() / len(df)

df2 = df.copy()

df2.drop(['salary_range', 'job_id', 'department', 'benefits'], axis = 1, inplace = True)

df2.head()


df2 = df2.sort_values('title').reset_index(drop = True)


df2.isna().sum()

df2['employment_type'] = df2['employment_type'].bfill(axis=0)
df2['required_experience'] = df2['required_experience'].bfill(axis=0)
df2['required_education'] = df2['required_education'].bfill(axis = 0)
df2['industry'] = df2['industry'].bfill(axis=0)
df2['function'] = df2['function'].bfill(axis=0)


df3 = df2.copy()

df3 = df3[df3['description'].notna()]


df3.isna().sum()


df3 = df3.dropna(axis = 0, how = 'any')

df3.shape

df3 = df3.drop_duplicates(keep = 'first')

df4 = df3.copy()

df4.head()


df4.shape

df4['description'] = df4['description'] + ' ' + df4['requirements'] + ' ' + df4['company_profile']
df4.drop(['company_profile', 'requirements'], axis = 1, inplace = True)

df4.head(3)

df4['country_code'] = df4['location'].str.split(',', expand=True)[0]
df4['city'] = df4['location'].str.split(',', expand = True)[2]


df4.head()

df4.loc[df4['city'] == ' ', 'city'] = np.nan

df4.isnull().sum()

df4.dropna(inplace = True)

import pycountry
list_alpha_2 = [i.alpha_2 for i in list(pycountry.countries)]
def country(df):
    if df['country_code'] in list_alpha_2:
        return pycountry.countries.get(alpha_2 = df['country_code']).name
df4['country_name'] = df4.apply(country, axis = 1)


df4.drop(['location', 'country_code'], axis = 1, inplace = True)

df4.head()


df4.shape


from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator



plt.figure(figsize = (20,20))
stopwords = set(STOPWORDS)
wc = WordCloud(background_color = "white", stopwords=stopwords, width = 1600 , height = 800 , max_words = 3000).generate(" ".join(df4[df4.fraudulent == 0]['description']))
plt.axis("off")
plt.imshow(wc , interpolation = 'bilinear')
plt.savefig('no_fraud_cloud.jpeg')


plt.figure(figsize = (20,20))
stopwords = set(STOPWORDS)
wc = WordCloud(background_color="white", stopwords=stopwords, width = 1600 , height = 800 , max_words = 3000).generate(" ".join(df4[df4.fraudulent == 1]['description']))
plt.axis("off")
plt.imshow(wc , interpolation = 'bilinear')
plt.savefig('fraud_cloud.jpeg')


df_clean = df4.copy()

df_clean.head()

df_clean.to_csv(r'Clean_data.csv')