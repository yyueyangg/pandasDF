import pandas as pd 
import numpy as np

print("Print pandas version")
print(pd.__version__)
print("")
print("-----------------")

exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)

# some attributes
print("Dataframe:")
print(df)
print("")

print("Index")
print(df.index)
print(df.index.values)
print(list(df.index.values))
print("")

print("Columns:")
print(df.columns)
print(df.columns.values)
print(list(df.columns.values))
print("")

print("Column types:")
print(df.dtypes)
print("")

print("Is dataframe empty:")
print(df.empty)
print("")

print("Dataframe shape:")
print(df.shape)
print("")

print("Dataframe size:")
print(df.size)
print("")

print("Values")
print(df.values)
print("")

print("Info")
print(df.info())
print("")

print("dtypes")
print(df.dtypes)
print("")

print("Attempts Sum")
print(df['attempts'].sum())
print("")

print("Score Mean")
print(df['score'].mean())
print("")

print("Sort Score in descending and ascending order")
df2 = df.sort_values(by=['score'], ascending=False)
print(df2)
df2 = df.sort_values('score', ascending=True)
print(df2)
print("")

# sort two things in the same df 
print("Sort attempts and names")
df2 = df.sort_values(by=['attempts', 'name'], ascending=True)
print(df2)
print("")

print("Reindex")
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
df3 = df2.reindex(labels=labels)
print(df3)
print("")

print("Map")
dict = {'yes':True, 'no':False}
df['qualify'] = df['qualify'].map(dict)
print(df)
print("")

print("Rename")
df.rename(columns=({'attempts':'noOfAttempts'}), inplace=True)
print(df)
print("")

print("Replace")
df2 = df.replace(np.nan, 0)
print(df2)
print("")

print("Using where to filter")
# set a condition, if the condition is not met, values will be replaced with other=
student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Age': [20, 21, 19], 'Marks': [85.10, 77.80, 91.54]}
df = pd.DataFrame(student_dict)
print(df)
filter = df['Marks'] > 80
df['Marks'].where(filter, other=1, inplace=True)
print(df)
print("")