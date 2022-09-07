def add(x,y):
    c=x+y
    return c
def sub(x,y):
    c=x-y
    return c
def mul(x,y):
    c=x*y
    return c
def div(x,y):
    c=x/y
    return c
while True:
    a=float(input("enter the first number"))
    b=float(input("enter the second number"))
    ch = input("enter the choice[+,-,*,/,** ]")
    if ch =="+":
        print("the added value",add(a,b))
    elif ch =="-":
        print("the subtracted value",sub(a,b))
    elif ch =="*":
        print("the multipled value",mul(a,b))                                          
    
    elif ch =="/":
              print("the divided vlaue ",div(a,b))
    elif ch == "**":
             print("the power value",pow(a,b))
    else:
             print("invalid choice")
