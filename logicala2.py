n=list(map(int,input("enter the list elements: ").rstrip().split()))
minimum=[]
maximum=[]
l=[]
for i in n:
    l.append(i)
    s=None
    m=None
    for j in l:
        if s==None:
            s=j
        elif j<s:
            s=j
        if m==None:
            m=j
        elif j>m:
            m=j
    minimum.append(s)
    maximum.append(m)
c_s=0
c_l=0
s_l=[]
lar_l=[]
for i in range(0,len(maximum)):
    if minimum[i] not in s_l:
        s_l.append(minimum[i])
        c_s+=1
    if maximum[i] not in lar_l:
        lar_l.append(maximum[i])
        c_l+=1
print(c_l-1,c_s-1)
# 10 5 20 20 4 5 2 25 1
# o/p:2 4

# 3 4 21 36 10 28 35 5 24 42
# 4 0