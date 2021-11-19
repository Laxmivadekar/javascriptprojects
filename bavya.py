# a=[19, 10, 12, 10, 24, 25, 22]
# k=int(input("enter the divisire: "))
# i=0
# c=0
# l=[]
# while i<len(a):
#     j=i
#     s=[]
#     while j<len(a)-1:
#         sum=a[i]+a[j+1]
#         if sum%k !=0:
#             s.append(a[i])
#             s.append(a[j+1])
#         j+=1
#     print(list(set(s)))
#     i=i+1
#     l.append(s)
# print(l)

# n=int(input("enter the number: "))
n=int(input("enter the number: "))
i=1
while i<=n:
    j=0
    while j<=i:
        if i==0:
            print(0,end="")
        print(1,end="")
        j+=1
    i+=1
    print()
# 1 
# 0 1 
# 1 0 1 
# 0 1 0 1 
# 1 0 1 0 1 
# 0 1 0 1 0 1
