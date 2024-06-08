import pandas as pd
import numpy as np
# pandas has two data structures : dataframes - refer to entire table , series - refer to a column or a row
df = pd.read_csv('matches.csv')
print(df.head(10))  # by default prints top 5, tail() prints bottom 5
print("\n data type of the table = ",type(df))
print("\nno of rows and columns of the data : ",df.shape)
print("\nbasic info abt the dataset :")
df.info()   # tells the data type of data in columns , number of non null entries
# pandas calls strings as object

print("\n",df.describe()) # shows mathematical data only in int and float data types(basically numerical columns)
print("\naccessing column : \n",df['winner'])  #this datatype is series as single column is being accessed
print("\nmultiple columns : \n",df[['team1','team2','winner']])
print("\naccesing row : \n",df.iloc[2])
print("\nmultiple rows : \n",df.iloc[1:12:3]) #access using slicing and even fancy indexing can be used
print("\nrows and columns using iloc :\n",df.iloc[[4,6,3],[3,7,10,12]]) # (rows,colmns) for fancy indexing another set of []

mask1 = df['city'] == "Pune"
mask2 = df['date'] > '2015-01-01'
mask3 = df['umpire1'] == "AY Dandekar" #masking is used to filter out using our desired data
print("\n list of matches played in pune after 2015 with AY Dandekar as umpire 1 : \n",df[mask1 & mask2 & mask3])

print("\nnumber of times a team has won a match :\n",df.value_counts('winner')) # used for categorical data,not in data which is random and varying

max_played = df['team2'].value_counts() + df['team1'].value_counts()
print("\nmax times played by which team : \n", max_played.sort_values(ascending=False)) # we can sort the values in ascending or descending order
print("\nsorting data, city as first priority in ascending, then in each city date as second priority in descending :\n\n",df.sort_values(['city','date'],ascending=[True,False]))

print("\ndata with unique attr,cleaning all dupilcate occurence :\n",df.drop_duplicates(subset = ['city'], keep = 'first', inplace=False)) 
#keeps first occurence, could have kept the last occurence
#alll these changes made in data is not permanent i.e. we can retrieve the original dataset by calling data 
# to make permanent changes we use the the attribute 'inplace=True' inside any operations

print("\n",df.drop_duplicates(subset='season',keep='last')[['season','winner']].sort_values('season'))

import matplotlib.pyplot as plt
df['toss_decision'].value_counts().plot(kind = 'pie')
# plt.show()

df['win_by_wickets'].plot(kind='hist')
# plt.show()
'''---------------------------------------------------------------------------------------------------------------------------------------------------'''
data = pd.read_csv('Companies.csv')
print("\n new dataset : \n")
print("\n",data.head())
sector = data.groupby('Sector')
print(sector,"\tlength of sector : ", len(sector) ,"\n", sector.size().sort_values(ascending=False))
print("\n",sector.first()) #name of companies in each sector which occurs at the first postion
print('\n',sector.groups) #returns dictionary with key as sector and value as indexing of tht company position
print('\n',sector.get_group('Apparel'))
print('\n',sector['Revenues'].mean().sort_values(ascending=False))
# learn isin() in pandas from the tutorial

df1 = pd.read_csv('deliveries.csv')
print("new dataset :\n",df1.head())
run = df1.groupby('batsman')  # works on categorical data which can be clubbed together on a specific parameter
print("\n",run['batsman_runs'].sum())

mask = df1['batsman_runs']==6
print("\n",df1[mask])

#to find which batsman made run most against which team
vk = df1[df1['batsman']== 'V Kohli']
print("most balls playedby Kohli against : \n",vk.groupby('bowling_team')['batsman_runs'].sum().sort_values(ascending = False))

# to access index  = series[].index()  and for value = series[].values()           .tolist() converts the index output in a list
# isin() function checks if condition given is present in the list given a slist input in argument
df_merged = df1.merge(df,left_on='match_id',right_on='id')
print("\nmerged dataframe :\n",df_merged.head(10))

print("wow:\n",df_merged.groupby(['season','batsman'])['batsman_runs'].sum().reset_index().drop_duplicates(subset='season',keep='first').sort_values('season'))

six = df1[df1['batsman_runs']==6]
pt = six.pivot_table(index='over',columns='batting_team',values='batsman_runs',aggfunc = 'count')
print("\npivot table : \n",pt)

import seaborn as sns
sns.heatmap(pt)
# plt.show()

# .corr() function is used to find the the correlation between two quantities it can be postive ,zero or even negative 
print(df1.rename(columns = {'batting_team':'bat_team','bowling_team':'bowl_team'}).head())    #renaming any complex name
print("\n",df1.set_index('batting_team').head())  # sets tht column as index and drops it from the dataset
# reset_index reverts the above operations , it is also used to provide indexing to a series and convert it to a dataframe
