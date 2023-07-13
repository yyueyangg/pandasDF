import pandas as pd 
import numpy as np

print("Dataframe with random values")
df1 = pd.util.testing.makeDataFrame()
print(df1)
print("")

print("Dataframe with missing values")
df2 = pd.util.testing.makeMissingDataframe()
print(df2)
print("")

print("Dataframe with datetime value")
df3 = pd.util.testing.makeTimeDataFrame()
print(df3)
print("")

print("Dataframe with mixed values")
df4 = pd.util.testing.makeMixedDataFrame()
print(df4)
print("")

print("Dataframe with date index")
sdata = {"c1":[120, 130 ,140, 150, np.nan, 170], "c2":[7, np.nan, 10, np.nan, 5.5, 16.5]}
df = pd.DataFrame(sdata)
print(df)
df.index = pd.util.testing.makeDateIndex()[0:6]
print(df)
df.interpolate(inplace=True)
print(df)