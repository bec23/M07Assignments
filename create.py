import pandas as pd

#create
df = pd.read_csv('telco_churn.csv')
tempdict={'col1':[1,2,3], 'col2':[4,5,6], 'col3':[7,8,9]}
dictdf=pd.DataFrame.from_dict(tempdict)

#read
df.head(10)
dictdf.head()
df.tail()

#show columns & data types
df.columns
df.dtypes

#summary statistics
df.describe
df.describe(include='object')

#filtering columns
df.State
df['International plan']
df[['State', 'International plan']]
df.State.unique()
df.Churn.unique()

#filtering on rows
df.head()
df[df['International plan']=='No']
df[(df['International plan']=='No') & (df['Churn']==False)]

#indexing with iloc
df.icloc[14]
df.iloc[14,-1]
df.iloc[22:33]

#indexing with loc
State=df.copy()
State.set_index('State', inplace=True)
State.head()
State.loc['OH']

#update dropping rows
df.isnull().sum()
df.dropna(inplace=True)
df.isnull().sum()

#dropping columns
df.drop('Area code', axis=1)

#creating calculated columns
df['New Column']=df['Total n ight minutes']+df['Total intl minutes']
df.head()

#updating an entire column
df['New Column']=100
df.head()

#updating a single value
df.iloc[0,-1]=10
df.head()

#condition based updating using apply
df['Churn Binary']=df['Churn'].apply(lambda x:1 if x==True else 0)
df.head()
df(df['Churn']=True).head()

#output to csv
df.to_csv('output.csv')

#output to json
df.to_json()

#output to html
df.to_html()

#delete a datafram
del df