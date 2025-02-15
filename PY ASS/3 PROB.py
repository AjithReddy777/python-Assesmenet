a=input().split(",")

d=[]
for i in a:
    if len(i)>1:
        r=i[-1]
        f=ord(r)
        d+=[f]
    else:
        f=ord(i)
        d+=[f]
d.sort() 
v=[]
for i in d:
    v+=[chr(i)]
print(v)

# or 
a=input().split(",")
a.sort()
print(a)
    


