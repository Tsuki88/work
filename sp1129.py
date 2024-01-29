# -*- coding: utf-8 -*-

import json

fn='白沙鄉民國83年-86年度人口統計表.json'

with open(fn,'r') as jx:
    
    data=json.load(jx)
    
list1=[]

for getdd in data:
    
    country=getdd['白沙鄉']
    fcnt=getdd['民國83年-女-人數']
    list1.append(int(fcnt))
    
    print(country,"：",fcnt)
    
print("總計：",sum(list1))