a=int(input("enter num:"))
if a>1:
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            print("not prime")
        else:
            print("primenum")
else:
    print("not prime")