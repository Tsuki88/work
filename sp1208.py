# -*- coding: utf-8 -*-
import pandas as pd

city=['紐約','曼谷','東京','台北','香港']

n1=[1000,600,950]
n2=[850,1150,860]
n3=[800,860,990]
n4=[1500,1000,960]
n5=[600,950,800]
n6=[800,180,980]

data1=[n1[0],n2[0],n3[0],n4[0],n5[0],n6[0]]
data2=[n1[1],n2[1],n3[1],n4[1],n5[1],n6[1]]
data3=[n1[2],n2[2],n3[2],n4[2],n5[2],n6[2]]

df1=pd.DataFrame([data1,data2,data3],columns=city,index=range(0.5))

print(df1)