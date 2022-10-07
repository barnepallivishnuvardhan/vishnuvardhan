n=input("enter the string")
count=0
for char in n:
    if char.lower() in "aeiou":
       print("vowels",char)
       count=count+1   
print("n.of vowels",count)
