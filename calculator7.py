def calculator():
    a=float(input("enter a:"))
    b=float(input("enter b:"))
    op=input("choose any symbol like (+,-,*,/):")
    if op== "+":
        print("addition result:",a+b)
    elif op == "-":
        print("subtraction result:",a-b)
    elif op == "*":
        print("multiplication result:",a*b)
    elif op == "/":
        print("division result:",a/b)
    else:
        print("try again")
calculator()

