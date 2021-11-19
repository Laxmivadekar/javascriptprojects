n=int(input("enter the number"))
l=[]
for i in range(0,n):
    l.append(list(map(int,input('enter the list numbers: ').rstrip().split())))
print(l)