'''F(0) =0
F(1) =1
 
F(2)=f(1)+f(0)=1+0=1
F(3)=F(2)+F(1)=1+1=2
generate fibonacci series for n number without recursive
'''
def fib(n):
    l=[0,1]
    for i in range(2,n):
       l.append((l[-1]+l[-2]))
    return l
print(fib(4))
        