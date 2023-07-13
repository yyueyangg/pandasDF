import pandas as pd 
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
print(df)

# iloc 
# use to get the respective rows and columns by specifying the index of rows / columns 
print("------------Using iloc---------------")
print(df.iloc[0:3]) # slicing 
print("")
print(df.iloc[[1, 3, 5, 7], [1, 2]])
print("")
print("-----------------------------")

# loc
# loc[2:3] will display both row 2 and row 3 
# while iloc[2:3] will only display row 2 
# loc require name of the rows & columns to select 
# iloc uses index 
print("-----------------using loc-------------------")
df2 = df.loc['a']
print(df2)
print("")
print(df.loc[:, ['name', 'score']])
print("")
print("-----------------------------")

# reverse orders
print("-------------reverse------------")
df1 = df.loc[:, ::-1]
print(df1)
df2 = df.loc[::-1, :]
print(df2)
df3 = df.loc[::-1, ::-1]
print(df3)
df4 = df.iloc[:, ::-1]
print(df4)
df5 = df.iloc[::-1, :]
print(df5)
df6 = df.iloc[::-1, ::-1]
print(df6)
print("")
print("-----------------------------")
# this means print until second last row or columns 
# df4 = df.iloc[:-1] / df4 = df.iloc[:, :-1]

# using get 
print("----------get------------")
print(df.get(['name', 'score']))
print("")
print("-----------------------------")

# using double square brackets
print("-------brackets--------")
print(df[['name', 'score']])
print("")
print("-----------------------------")


# using at to locate something 
print("---------------at---------------")
print(df)
print(df.at['d', 'score'])
df.at['d', 'score'] = 11.5
print(df)
print("")
print("-----------------------------")

# using iat 
# similar to iloc and loc, iat uses index 
print("--------------iat--------------")
print(df.iat[8, 1])
df.iat[8, 1] = 20
print(df.iat[8, 1])
print("")
print("-----------------------------")

# filter 
# filter by setting a condition
print("-----------filter1.0--------------")
df2 = df[df['attempts']>2]
print(df2)
print("")
print("-----------------------------")

# using loc to filter 
print("-------------filter2.0--------------")
print(df.loc[df['score']>15])
print("")
print("-----------------------------")

# number of rows and number of columns 
# df.axes[0] = rows, [1] = columns and put the labels into a list
print("----------rows and columns-------------")
print(len(df.axes[0]))
print(df.axes[1])
print(len(df.columns))
print(len(df.index))
print("")
print("-----------------------------")

# check for nulls 
# can fill null values with fillna()
print("-----------nulls----------")
df2 = df['score'].isnull()
print(df2)
df2 = df[df['score'].isnull()]
print(df2)
print("")

df3 = df['score'].isna()
print(df3)
df3 = df[df['score'].isna()]
print(df3)
print("-----------------------------")

# check for values that are between certain range 
print("----------between---------")
df2 = df['score'].between(15, 20)
print(df2)
df2 = df[df['score'].between(15, 20)]
print(df2)
print("")
print("-----------------------------")

# using & 
print("-----------&------------")
df2 = (df['attempts']<2) & (df['score'] > 15)
print(df2)
df2 = df[(df['attempts']<2) & (df['score']>15)]
print(df2)
print("")
print("-----------------------------")

# iterrows returns each index and row in each iteration 
print("------------iterrows-----------")
for index, row in df.iterrows():
    print(index, row)
print("")
print("-----------------------------")

# fraction using sample and drop 
print("------------frac--------------")
dff = pd.DataFrame(np.random.randn(10, 2))
print("Original DataFrame:")
print(dff)

part70 = dff.sample(frac=0.7)
part30 = dff.drop(part70.index)
print(part70)
print(part30)
print("")
print("-----------------------------")

# shuffle using frac = 1 
print("-----------shuffle-----------")
shuffleddf = df.sample(frac=1)
print(shuffleddf)
print("")
print("-----------------------------")

# locate index of columns and rows 
print("--------get_loc--------")
print(df.columns.get_loc('score'))
print(df.index.get_loc('d'))
print("")
print("-----------------------------")

# return the first n rows with the largest values 
print("-----------nlargest------------")
df1 = df.nlargest(3, 'attempts')
df2 = df.nlargest(3, 'score')
print(df1)
print(df2)
print("")
print("-----------------------------")

# select certain dtypes 
print("------------select dtype----------")
df1 = df.select_dtypes(include='float64')
print(df1)
df2 = df.select_dtypes(exclude=object)
print(df2)
print("")
print("-----------------------------")

# cut into diff groups 
print("-----------cut------------")
df1 = df.fillna(1)
df['score_group'] = pd.cut(df['score'], bins=[0, 10, 15, 20], labels=['lousy', 'average', 'good'])
print(df['score_group'])
print("")
print("-----------------------------")

# factorize
print("----------factorize----------")
df2 = pd.factorize(df['name'])
print(df2)
index, name = df2
print(index)
print(name)
print("")
print("-----------------------------")


