l=[5,4,3,2,1]
i=1
while i<len(l):
    if l[i]<l[i-1]:
        l[i-1]=l[i]
        l[i]=l[i-1]
    i+=1
print(l)