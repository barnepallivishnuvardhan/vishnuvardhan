number=int(input("enter a number"))
rev=0
while( number>0):
           remainder=( number % 10)
           rev=(rev*10+remainder)
           number=number//10
print(rev)
