# modify display settings 
import pandas as pd
import numpy as np
print(pd.get_option('display.max_row'))
print(pd.get_option('display.max_column'))
print(pd.get_option('display.width'))
pd.set_option('display.max_row', 500)
pd.set_option('display.max_column', 500)
pd.set_option('display.width', 1000)
print(pd.get_option('display.max_row'))
print(pd.get_option('display.max_column'))
print(pd.get_option('display.width'))