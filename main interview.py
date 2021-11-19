# 3
# 2
# 4 8
# 15 30
# 25 50
A=[[4,8],[15,30],[25,50]]
# c=0
# i=0

# while i<len(a):
#     j=i+1
#     k=0
#     while k<=0:
#         if (a[i][0]*a[j][0]==a[i][1]*a[j][0]):
#             c+=1
#         k+=1
#     i+=1
# print(c)

# res = 0
 
# for i in range(len(A)):
#     for j in range(i + 1, len(A), 1):
#         if (A[i][0] * A[j][1] ==
#             A[i][1] * A[j][0]):
#             res += 1
# print(res)

# a=["a","e","i","o","u"]
# s="azerdii"
# l=s.split()
# k=5
# st=""
# i=0
# c=0
# while i<k:
#     st+=l[0:5]
#     if ("a"in st):
#         c+=1
#     if ("e" in st):
#         c+=1
#     if ("i" in st):
#         c+=1
#     if ("0" in st):
#         c+=1
#     if ("u" in st):
#         c+=1
#     l.remove(l[0])
#     i+=1
# if c>=3:
#     print(c)
# else:
    # pass

# s="azerdii"
# k=5
# vowels=['a','e','i','o','u']
# split=s.split()
# c=0
# for letter in s:
#     if len(split)>=k:
#         count=0
#         sub_str=""
#         for l in range(0,k):
#             if s[l] in vowels:
#                 count+=1
#             sub_str+=s[l]
#         if c<=count:
#             c=count
#             # sub=sub_str
#             print(sub_str)
#         split.remove(letter)
# print(sub)

'''a="aWESOME is cODING"
c=a.split()
j=-1
s=""
for i in c:
    b=c[j]
    st=""
    for i in b:
        if i.isupper()==True:
            st+=i.lower()
        else:
            st+=i.upper()
    s+=st+" "
    j-=1
print(s)'''
# a="A"
# if a.isupper()==True:
#     print("lucky")
import math
class Rectangle:
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        return self.breadth*self.length

    pass

class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return math.pi*(self.radius**2)
    pass  





