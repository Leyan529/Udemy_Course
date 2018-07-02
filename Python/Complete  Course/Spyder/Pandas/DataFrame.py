# -*- coding: utf-8 -*-
import pandas as pd

Vedios_List = {
        "Name":["SUMMER RAIN","LOVE WHISPER","FINGERTIP","NAVILLERA","ROUGH"],
        "Date":["2017-09-13","2017-08-01","2017-03-06","2016-07-10","2016-01-24"],
        "Url":["k7npTim4Xj4","wctRcg67E_g","hRPrpLSo4To","1ZhDsPdvl6c","r_6q_-d-7Sk"],
        "ViewCount":[1251798,2542617,1670381,2388747,1313804]
        }


GFRIEND_Vedios_List = pd.DataFrame(
        Vedios_List,
        columns =["Name","Date","Url","ViewCount"])
print(GFRIEND_Vedios_List)