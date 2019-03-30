def is_prime(c):

    counter=0
    for i in range(1,c+1):
        if c%i==0:
            counter=counter+1
    if counter==2:
        c=c**0
        return c
    else:
        c=c*0
        return c

while True:
    try:
        num=int(input("digite el numero"))
        if num < 0:
            print("el numero es menor que cero, no se puede")
            break
        prime=is_prime(num)
        if prime==0:
            print(prime)
        else:
            print(prime)
    except Exception:
        print("-1")
                       
        
