def is_prime(c):

    counter=0
    for i in range(1,c+1):
        if c%i==0:
            counter=counter+1
    if counter==2:
        print("the number is prime")

    else:
        print("is NOT a prime number")

num=int(input("digite un numero"))
is_prime(num)
        
