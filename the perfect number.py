def perfect_number(num):

    x=0
    for i in range(1,num):
        if num%i==0:
            x+=i
    if x==num:
        print("the number is perfect")
    else:
        print("the number is not perfect")

num=int(input("digite un numero"))
perfect_number(num)
        
