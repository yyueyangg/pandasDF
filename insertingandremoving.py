import pandas as pd 
import numpy as np
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)

# insert 
print("---------------inserting--------------")
print("Inserting through indexing")
new = {'name' : ["Suresh"], 'score': [15.5], 'attempts': [1], 'qualify': ["yes"]}
label = ['k']
df2 = pd.DataFrame(new, index=label)
df3 = df.append(df2)
print(df3)
print("")

# can use iloc also 
print("Inserting through loc")
df.loc['k'] = ['Suresh', 15.5, 1, 'yes']
print(df)
print("")

print("Inserting through insert")
color = ['Red','Blue','Yellow', 'Orange','Red','White','White','Blue','Green','Green','Red']
df.insert(2, 'COLOURS', color) # index, name, insert
print(df)
print("")


# drop rows and columns
print("-----------drop(rows and columns)---------------")
print("Drop a row")
df.drop('e', inplace=True)
print(df)
df.reset_index(inplace=True)
print(df)
print("")

print("Drop multiple columns")
df2 = df.drop(columns=['score', 'attempts'])
print(df2)
print("")

print("Drop using axis=0")
df2 = df.drop(0, axis=0)
print(df2)
print("")

print("Drop using axis=1")
df2 = df.drop('name', axis=1)
print(df2)
print("")

print("Drop using iloc") # can drop with loc, but specify name of rows / columns 
df2 = df.drop(columns=df.iloc[:, 4:])
print(df2)
print("")

print("Drop with del")
del df['score']
print(df)
print("")

print("Drop with pop")
df.pop('attempts')
print(df)
print("")

print("Drop from multiindex")
col = pd.MultiIndex.from_arrays([['Class A', 'Class A', 'Class B', 'Class B'], 
                                 ['Name', 'Marks', 'Name', 'Marks']])

student_df = pd.DataFrame([['Joe', '85.10', 'Nat', '77/.80'], ['Harry', '91.54', 'Sam', '68.55']], columns=col)
print(student_df)
df1 = student_df.drop(columns='Class B', level=0)
print(df1)
df2 = student_df.drop(columns='Marks', level=1)
print(df2)
print("")
print("-----------------------")


# drop duplicates 
print("---------drop(duplciates)-----------")
print("Drop everything except first copy")
student_dict = {"name": ["Joe", "Nat", "Harry", "Joe", "Nat"], "age": [20, 21, 19, 20, 21],
                "marks": [85.10, 77.80, 91.54, 85.10, 77.80]}
df = pd.DataFrame(student_dict)
print(df)
print("")
df1 = df.drop_duplicates()
print(df1)
print("")

# keep is always defaulted to first
print("Drop everything except last copy")
df2 = df.drop_duplicates(keep='last')
print(df2)
print("")

print("Drop all")
df3 = df.drop_duplicates(keep=False)
print(df3)
print("")

# drop certain columns using subsets 
print("Drop certain columns")
student_dict = {"name":["Joe","Nat","Harry","Sam" ], "age":[20,21,19,21], "marks":[85.10, 77.80, 91.54, 77.80]}
df = pd.DataFrame(student_dict)
print(df)
print("")
df1 = df.drop_duplicates(subset=['age'])
print(df1)
print("")

# reset index
print("Drop and reset index")
student_dict = {"name": ["Joe", "Nat", "Harry", "Nat"], "age": [20, 21, 19, 21], "marks": [85.10, 77.80, 91.54, 77.80]}
df = pd.DataFrame(student_dict, index=['a', 'b', 'c', 'd'])
print(df)
print("")
df1 = df.drop_duplicates(keep=False, ignore_index=False)
print(df1)
print("")
df2 = df.drop_duplicates(keep=False, ignore_index=True)
print(df2)
print("")
print("-------------------")

# dropping na / null / np.nan values using dropna
print("-----------drop(na)-------------")

print("Drop axis=1")
student_dict = {"name": ["Joe", "Sam", "Harry"], "age": [20, 21, 19], "marks": [85.10, np.nan, 91.54]}
df = pd.DataFrame(student_dict)
print(df)
print("")
df1 = df.dropna(axis=1)
print(df1)
print("")

print("Drop axis=columns")
df2 = df.dropna(axis='columns')
print(df2)
print("")

# setting number non null values with thresh, else drop column
print("Drop by thresh")
student_dict = {"name": ["Joe", "Sam", np.nan, "Harry"], "age": [np.nan, np.nan, np.nan, np.nan],
                "marks": [85.10, np.nan, np.nan, 91.54]}
df = pd.DataFrame(student_dict)
print(df)
print("")
df1 = df.dropna(axis=1, thresh=3)
print(df1)
print("")

# fill in na values 
print("Fill in na values")
print(df.isnull())
df.fillna(0, inplace=True)
print(df)
print("")
