i=0 #控制循环
while i==0: #本质是构造一个可以一直进行循环的条件
    x=eval(input())
    if x==000: #判断输入是否为000
        i=1 #若是则将i赋值以停止循环
    else:
        b=x%5
        c=x%7
        if b==0 and c==0: #and为和语句，意为同时成立
            print("yes")
        else:
            print("no")