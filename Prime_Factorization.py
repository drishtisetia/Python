n = int(input("What is your number? :"))
a=n//2
b=[]
print(len(b))

for i in range(2,a):
    if(n%i==0):
        if len(b)==0:
            b.append(i)
        else:
            for j in range(0,len(b)):
                if(i%b[j]!=0):
                    b.append(i)
    else:
        pass

print(b)
