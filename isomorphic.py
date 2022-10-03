s=input()
t=input()
if(len(s)!=len(t)):
    print("false")
else:
    d={}
    for i in range(len(s)):
        if(s[i] not in d):
            d[s[i]]=t[i]
    St=""
    for i in range(len(s)):
        St=St+d[s[i]]
    if(St==t):
        print("True")
    else:
        print("false")
        
    
