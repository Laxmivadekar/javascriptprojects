# a="baab"
# l=[]
# for i in range(0, len(a)):
#     l.append(a[i])
# print(l)
# i=1
# while i<len(l):
#     if l[i]==l[i-1]:
#         if len(l)==2:
#             print('Empty String')
#         l.remove(l[i])
#         l.remove(l[i-1])
#     print(l)
#     i+=1
# s=""
# for j in l:
#     s+=j
# print(s)

import sys

def super_reduced_string(s):
    if len(s) == 1:
        return s
    ind = 1
    while ind < len(s):
        #print("s[{}] = {} s = {}".format(ind, s[ind], s))
        if s[ind] == s[ind-1]:
            if len(s) == 2:
                return 'Empty String'
            s = s[:ind-1] + s[ind+1:]
            ind = 1
        else:
            ind += 1
            
    if len(s) == 0:
        return 'Empty String'
    else:
        return s
s = input("enter the string: ").strip()
result = super_reduced_string(s)
print(result)



