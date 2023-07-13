import pandas as pd 

# convert list to df 
print("Convert list to df")
fruits_list = ['Apple', 'Banana', 'Orange','Mango']
df = pd.DataFrame(fruits_list, index=['f1', 'f2', 'f3', 'f4'], columns=['Fruits'])
print("List1")
print(df)


fruits_list = [['Apple', 'Banana', 'Orange', 'Mango'],[120, 40, 80, 500]]
df1 = pd.DataFrame(fruits_list)
print("Hierarchical list1")
print(df1)

df2 = pd.DataFrame(fruits_list).transpose()
print("Hierarchical list2")
print(df2)

fruits_list = ['Apple', 'Banana', 'Orange', 'Mango']
price_list = [120, 40, 80, 500]
list1 = list(zip(fruits_list, price_list))
df3 = pd.DataFrame(list1)
print("Multiple list")
print(df3)
print("")
print("---------------------")

# convert dict to df 
print("Convert dict to df")
fruits_list = ['Apple', 'Banana', 'Orange', 'Mango']
price_list = [120, 40, 80, 500]
fruits_dict = {'Fruits': fruits_list, 
               'Price': price_list}
df = pd.DataFrame(fruits_dict)
print(df)

# multi level (nested) dict 
print("Convert nested dict to df")
student_dict = {"Grade A": {'Class A': {'name': 'Joe', 'marks': 91.56},
                            'Class B': {'name': 'Harry', 'marks': 87.90}},
                "Grade B": {'Class A': {'name': 'Sam', 'marks': 70},
                            'Class B': {'name': 'Alan', 'marks': 65.48}}}
df1 = pd.DataFrame(student_dict)   
print(df1)
df2 = pd.DataFrame.from_dict({(i, j): student_dict[i][j] 
                              for i in student_dict.keys()
                              for j in student_dict[i].keys()})
print(df2)
df3 = pd.DataFrame.from_dict({(i, j): student_dict[i][j]
                              for i in student_dict.keys()
                              for j in student_dict[i].keys()}, orient='index')
print(df3)
print("")
print("---------------------")

# convert df to dict (6 ways)
df = pd.read_csv("StudentData.csv")
print(df)

sd1 = df.to_dict()
print("dict")
print(sd1)

sd2 = df.to_dict('list')
print("list")
print(sd2)

sd3 = df.to_dict('series')
print("series")
print(sd3)

sd4 = df.to_dict('split')
print("split")
print(sd4)

sd5 = df.to_dict('records')
print("records")
print(sd5)

sd6 = df.to_dict('index')
print("index")
print(sd6)

print("")
print("---------------------")

# convert datatype 
print("Convert data type")
student_dict = {"name": ["Joe", "Nat", "Harry"], "age": [20, 21, 19], "marks": [85.10, 77.80, 91.54]}
student_df = pd.DataFrame(student_dict, dtype='float64') # change of dtype for age 
print(student_df)
print("")
print("---------------------")
