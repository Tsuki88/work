# -*- coding: utf-8 -*-
import time

print("歡迎登入系統！")
counter=0

while   True:

    counter=counter+1
    usrid=input("請輸入帳號：")
    usrpwd=input("請輸入密碼：")

    print("驗證第",counter,"次")

    if usrid=="kid1412" and usrpwd=="0621":
    
        print("成功登入，請稍後…")
        break

    else:
        
        xtime=time.localtime()
        tmsg=str(xtime[0])+str(xtime[1])+str(xtime[2])+str(xtime[3])+str(xtime[4])+str(xtime[5])
    
        files=tmsg+'.txt'
        fb=open(files,'w',encoding='utf-8')
        fb.write("輸入帳號："+usrid)
        fb.write("輸入室碼："+usrpwd)

    if counter>=3:
        print("帳號密碼輸入錯誤，請重新輸入！")
        break