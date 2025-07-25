# def armstrong(n):
#     a=str(n)
#     power=len(a)
#     total=0
#     for i in a:
#         total+=int(i)**power
#     if total==n:
#         print("amstrong")
#         return True
#     else:
#         print("not amstrong")
#         return False
# n=int(input("enter num:"))
# armstrong(n)

def armstrong(n):
    temp=n
    power=len(str(n))
    total=0
    while temp>0:
        digit=temp%10
        total+=digit**power
        temp=temp//10
    if total==n:
        print("amstrong")
        return True
    else:
        print("not amstrong")
        return False
n=int(input("enter num:"))
armstrong(n)

