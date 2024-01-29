# -*- coding: utf-8 -*-
import random
import time

print("系統開始時間：",time.asctime())
start=time.time()

min=int(input("請輸入A值："))
max=int(input("請輸入B值："))

res=random.randint(min,max)

while True:
    
    msg="請輸入"+str(min)+"-"+str(max)+"的數字"
    
    guess=int(input(msg))
    
    if guess==res:
        end=time.time()
        print("恭喜答對")
        print("共花了"+str(int(end-start))+"秒")
        
        
        break
    
    
    elif guess<res:
        print("請猜大一點")
        
    else:
        print("請猜小一點")