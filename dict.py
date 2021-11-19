a={1:"shailu",3:"lucky",2:"sappy"}
b=list(a.keys())
b.sort()
d={}
for i in b:
    for j in a:
        if i==j:
            d[i]=a[j]
print(d)
