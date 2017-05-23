from pandas import *
import pandas as pd
import numpy as np
from pandas import compat 

#Drops NA so that it can just skip blank cells
def dropna(self,data):
  return dict((k, v.dropna().to_dict()) for k, v in compat.iteritems(data))

xls = ExcelFile('data.xlsx')
df = xls.parse(xls.sheet_names[0])
data = pd.DataFrame(df.to_dict())
dict = dropna(dict, data)

ratings = dict
