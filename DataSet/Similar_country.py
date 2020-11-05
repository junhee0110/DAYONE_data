import pandas as pd
import time
start = time.time()
from DataSet.Country_compare import *

Fat = pd.read_csv("Fat_Supply_Quantity_Data.csv")
Country=Corona_compare(Fat)
Country.calc(Fat)

print("time :", time.time() - start)

