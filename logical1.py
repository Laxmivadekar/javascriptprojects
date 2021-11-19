a=[["rahul"],["sheethal"],["himani"]]
l=[]
l1=[]
for i in a:
    for j in i:
        l.append(len(j))
        l1.append(j)
b=max(l)
for j in l1:
    if b==len(j):
        print(j,"max number is",b)
