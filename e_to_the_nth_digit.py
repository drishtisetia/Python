from decimal import *

getcontext().prec=1000000    #Change for prescision


def fact(n):
    k = 1
    for i in range(0, n-1):
        k = k*(n-i)
    return (k)



def inv(n):
    return(Decimal(1/n))



e = 0
i = 0
while(True):
    g=Decimal(fact(i))
    i+=1
    h=inv(g)
    e=e+h
    if(g>10**100):     #Change for accuracy
        break
print(e)
