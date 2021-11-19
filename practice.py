# a=int(input())
# l=list(map(str,input().rstrip().split()))[:a]
# print("actual list",l)
# s=set(l)
# print(s)
# print(len(s))
# for i in list(s):
#     c=0
#     for j in l:
#         if i==j:
#             c+=1
#     print(c,"",end="")
# print()

n=int(input())
l=[]
for i in range(0,n):
    u=input()
    l.append(u)
s=set(l)
print(len(s))
for i in list(s):
    c=0
    for j in l:
        if i==j:
            c+=1
    print(c,"",end="")









# o/p 3
# 2 1 1


# 4
# bcdef abcdefg bcde bcdef
