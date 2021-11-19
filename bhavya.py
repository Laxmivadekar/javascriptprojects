# a=[1,7,2,4]
a=[19, 10, 12, 10, 24, 25, 22]
k=int(input("enter the divisire: "))
i=0
c=0
while i<len(a):
    j=i
    while j<len(a)-1:
        sum=a[i]+a[j+1]
        if sum%k !=0:
            c+=1
        j+=1
    i=i+1
print(c)

# 1 + 7 = 8
# 1 + 2 = 3
# 1 + 4 = 5
# 7 + 2 = 9
# 7 + 4 = 11
# 2 + 4 = 6

# S = {1, 7, 4}
# S = [19, 10, 12, 10, 24, 25, 22]  k = 4