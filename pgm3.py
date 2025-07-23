# def factorial(n):
#     if n==0 or n==1:
#         return 1
#     return n*factorial(n-1)
# print(factorial(7))


# n=int(input("enter num:"))
# fact=1
# for i in range(1,n+1):
#     fact=fact*i
# print("factorial result:",fact)

# import math
# print(math.factorial(5))

n=int(input("enter:"))
i=1
fact=1
while i<=n:
    fact=fact*i
    i+=1
print("factorail:",fact)