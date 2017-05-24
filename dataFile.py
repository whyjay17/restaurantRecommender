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

print("다음 식당들에 대한 평점을 입력하시오 (10점 만점)")

print("맥도날드에 대한 평점을 입력하시오:")
mc = float(input())

print("KFC에 대한 평점을 입력하시오:")
kfc = float(input())

print("홍콩반점에 대한 평점을 입력하시오:")
hk = float(input())

print("아비꼬에 대한 평점을 입력하시오:")
abiko = float(input())

print("엉터리생고기에 대한 평점을 입력하시오:")
ung = float(input())

print("원할머니보쌈에 대한 평점을 입력하시오:")
won = float(input())

print("신선설농탕에 대한 평점을 입력하시오:")
sinsun = float(input())

print("포베이에 대한 평점을 입력하시오:")
pho = float(input())

print("애슐리에 대한 평점을 입력하시오:")
ash = float(input())

print("새마을식당에 대한 평점을 입력하시오:")
sae = float(input())

print("놀부부대찌개에 대한 평점을 입력하시오:")
nol = float(input())

ratings['currUser'] = {
	
	'맥도날드': mc,
	'KFC': kfc,
	'홍콩반점': hk,
	'아비꼬': abiko,
	'엉터리생고기': ung,
	'원할머니보쌈': won,
	'신선설농탕': sinsun,
	'포베이': pho,
	'애슐리': ash,
	'새마을식당': sae,
	'놀부부대찌개': nol
}

print(ratings['currUser'])