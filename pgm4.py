# def fibonacci(n):
#     a,b=0,1
#     for i in range(n):
#         print(a,end=" ")
#         a,b=b,a+b
# fibonacci(15)

# def fibonacci(n):
#     a,b=0,1
#     i=0
#     while i<n:
#         print(a,end=" ")
#         a,b=b,a+b
#         i+=1
# fibonacci(15)

def fibonacci(n):
    list=[]
    a,b= 0, 1
    count = 0
    while count < n:
        list.append(a)
        count += 1
        a, b = b, a + b
    return list
print(fibonacci(10))






