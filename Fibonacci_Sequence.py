def fib(n):
    a=1
    b=1
    arr = [a, b]
    for i in range(1,n):
       c=arr[i]+arr[i-1]
       arr.append(c)

    print(arr)


fib(100)
