'''                            Count
Game  Score  Minimum  Maximum   Min Max
    0      12     12       12       0   0
    1      24     12       24       0   1
    2      10     10       24       1   1
#     3      24     10       24       1   1'''
# minimum=[]
# maximum=[]
# a=list(map(int,input("enter the list elements: ").rstrip().split()))
# b=[]
# d=[]
# e=[]
# for j in range(0,len(a)):
#     b.append(j)
#     s=0
#     m=0
#     for i in b:
#         if s==0:
#             s=i
#         elif i<m:
#             s=i
#         if m==0:
#             m=i
#         elif i>m:
#             m=i
#     minimum.append(s)
#     maximum.append(m)
#     if maximum[j] not in d:
#         d.append(maximum[j])
#     if minimum[j] not in e:
#         e.append(minimum[j])
# print(maximum)
# print(minimum)
# print(d)
# print(e)
# print(len(d)-1)
# print(len(e)-1)







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
        elif j<m:
            s=j
        if m==None:
            m=j
        elif j>m:
            m=j
    minimum.append(s)
    maximum.append(m)
a=min(minimum)
b=max(maximum)
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
print(c_s-1,c_l-1)
'''scores=[12,24,10,24]
# scores=[10 ,5 ,20, 20, 4, 5, 2, 25, 1]
a=[]
minimum=[]
maximum=[]
for i in scores:
    a.append(i)
    s=0
    m=0
    for j in a:
        if s==0:
            s=j
        elif j<s:
            s=j
        if m==0:
            m=j
        elif j>m:
            m=j
    minimum.append(s)
    maximum.append(m)
print(minimum)
print(maximum)
min_l=[]
for i in minimum:
    if i not in min_l:
        min_l.append(i)
print("min_c",len(min_l)-1)
max_l=[]
for i in maximum:
    if i not in max_l:
        max_l.append(i)
print("min_c",len(max_l)-1)

# min_c=[]
# max_c=[]
# for i in range(0,len(minimum)):
#     if minimum[i]==b:
#         min_c.append(1)
#     else:
#          min_c.append(0)
#     if maximum[i]==c:
#         max_c.append(1)
#     else:
#         max_c.append(0)
# print("min",minimum)
# print("max",maximum)
# print("min_count:",min_c)                               #    9
#                                                         #10 5 20 20 4 5 2 25 1
# print("max_count:",max_c)
'''