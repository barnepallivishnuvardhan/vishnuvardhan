print("program to get perfect squares in given ranges")
n=int(input("enter the lower range"))
m=int(input("enter the upper range"))
a=[]
a=[x for x in range(n,m+1)
   if(int(x**0.5)**2==x) and sum(list(map(int,str(x))))<10]
print(a)
