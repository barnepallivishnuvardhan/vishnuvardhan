python=int(input("enter a python marks:"))
java=int(input("enter a java marks:"))
c=int(input("enter a c marks:"))
maths=int(input("enter a maths marks:"))
total=python+java+c+maths
print("total marks are:",total)
avg=total/4
print("average marks:",avg)
if(avg>=95 and avg<100):
    print("grade S,")
elif(avg>=90 and avg<95):
    print("grade A." )
elif(avg>=80 and avg<90):
    print("grade B.")
elif(avg>=70 and avg<80):
    print("grade C.")
elif(avg>=60 and avg<70):
    print("grade d.")
elif(avg>=50 and avg<60):
    print("grade e.")
else:
    print("fail")
    

