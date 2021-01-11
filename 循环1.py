#打印99乘法表
#h=1
#while h<=9:
#    l=1
#    while l<=h:
#        print("%d*%d=%d  "%(h,l,h*l),end="")#end=" "的作用是让print遇到空(即print(""))时换行
#        l+=1
#        pass 
#    print("")
#    h+=1
#    pass
#打印直角三角形
#row=10
#while row>=1:
#    col=1
#    while col<=row:
#        print("*",end="")
#        col+=1
#        pass
#    print("")
#    row-=1
#    pass
#打印等腰三角形
row=1
while row<=10:
    kg=1
    while kg<=10-row:
        print(" ",end="")
        kg+=1
        pass
    xh=1
    while xh<=2*row-1:
        print("*",end="")
        xh+=1
        pass
    print("")
    row+=1
    pass

    


