def is_prime(num):
    for n in range(2,num):
        if num % n ==0:
            print('Not prime')
        else:
            print('Number is prime')



is_prime(5)
