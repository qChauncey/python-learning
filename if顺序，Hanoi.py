def rec(n,a,b):
    if n ==1:
        print(a,b)
    else:
        print(n,a,b,0)
        rec(n-1,b,a)
        print(n,a,b,1)
        print(n,a,b,2)
n=int(input("pls:"))
rec(n,11,22)
#else下面，print 0居然先从5开始算了4次到2为止，输出回if内数据，然后再迭代从n=2开始（1从if内开始了），一直到5.但为什么只输出print 0结果但是却n-1了？



