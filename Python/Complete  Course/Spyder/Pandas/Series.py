# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
s = pd.Series(["BTS","GFRIEND","BTOB","TWICE"])
print(s)
print(s[2:4])

s = pd.Series(["BTS","GFRIEND","BTOB","TWICE"],
              index=["a","b","c","d"])
print(s)
print(s[2:4])

print("----------------------------------")

Group_list = [{'Name': 'GFRIEND Official', 'viewCount': 4000000,'Filter':'GFRIEND MV'}, #order_ByRelevance
              {'Name': 'BTS', 'viewCount': 5000,'Filter':'BTS'}, #order_ByRelevance
              {'Name': 'TWICE Official', 'viewCount': 20000900,'Filter':'TWICE'}, #order_ByRelevance
              {'Name': 'EXO SMTOWN', 'viewCount': 20000,'Filter':'EXO'}, #order_ByRelevance
              {'Name': 'Super Junior Official', 'viewCount': 25000,'Filter':'Super Junior'}, #order_ByRelevance
              {'Name': 'Lovelyz woolliment', 'viewCount': 30000,'Filter':'Lovelyz'} #order_ByRelevance
              ]

#pandas.Series(dict) : dict 轉Series物件 
#pandas.Series(dict) : return Series
for index,group in enumerate(Group_list):
    pd_group = pd.Series(group)
    print(pd_group)    
#    print("viewCount > 25000 ?" )
#    print(pd_group['viewCount']>25000)
    #Series(Series["Field"]>condition) : return [T|F]
    print("----------------")
    
Vedio_List={"SUMMER RAIN":100,
            "LOVE WHISPER":250, 
            "FINGERTIP":160,
            "NAVILLERA":230,
            "DOPE":560,
            "NOT TODAY":780,
            "DNA":430}
Vedio_Series = pd.Series(Vedio_List)
# Series(Series[Series > condition ) : 
# return match of part Series
print(Vedio_Series[Vedio_Series>167])
print("-----------------------------------")

Vedio_Series = pd.Series(Vedio_List)
print(Vedio_Series)
print(Vedio_Series<300)

print("-----------------------------------")
# update value like dict
# Series[key] = value
Vedio_Series["SUMMER RAIN"] = 5000000
print(Vedio_Series)
print("-----------------------------------")
# update value like dict
# Series[Series condition] = value
Vedio_Series[Vedio_Series<300] = 3000
print(Vedio_Series)
print("-----------------------------------")
# decide index in Series
print( "SUMMER RAIN" in Vedio_Series)
print( "Rough" in Vedio_Series)
print("-----------------------------------")
# 可群體計算
Vedio_Series /= 10 
print(Vedio_Series)
print("-----------------------------------")
# 轉numpy結構
square = np.square(Vedio_Series)
print(square)
print("-----------------------------------")
# Series群組判斷非空
print(Vedio_Series.isnull())























