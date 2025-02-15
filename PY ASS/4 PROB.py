a=input().split(",")
b=input().split(",")
print(a)
l=[]
k=[]
for i in  a:
    d=i
    if " " in d:
        
        if ":" in d:
            f=d.index(":")
            
            c=d[1:f]+d[f+1:]
            l+=[int(c)]
        
    else:
        if ":" in d:
            f=d.index(":")
            
            c=d[:f]+d[f+1:]
            l+=[int(c)]
for i in  b:
    d=i
    if " " in d:
        
        if ":" in d:
            f=d.index(":")
            
            c=d[1:f]+d[f+1:]
            k+=[int(c)]
        
    else:
        if ":" in d:
            f=d.index(":")
            
            c=d[:f]+d[f+1:]
            k+=[int(c)]
            
            
            

g=len(l)
y=1
l.sort()
k.sort()
for i in range(g-1):
    if k[i]<l[i+1]:
        y=y
    else:
        y+=1
print(y)
    
        
    