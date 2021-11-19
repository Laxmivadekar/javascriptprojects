# n,m=map(int,input("enter the numbers").split())
# Pattern=[]
# for i in range(n//2):
#     Pattern.append(".|."*(2*i+1).center(m,"-"))
# print(("\n".join(Pattern+["WELCOME".center(m,'-')])))


# n, m = map(int,input().split())
# pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))


'''
---------.|.---------      String: ".|."
------.|..|..|.------      String: ".|..|..|." (same as 3*".|.")
---.|..|..|..|..|.---      String: 5 * ".|."
.|..|..|..|..|..|..|.      (...)
-------WELCOME-------      String: "WELCOME"
.|..|..|..|..|..|..|.      (...)
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------'''
'''N, M = map(int,input().split())
for i in range(1,N,2): 
    print((i * ".|.").center(M, "-"))
print("WELCOME".center(M,"-"))
for i in range(N-2,-1,-2): 
    print((i * ".|.").center(M, "-"))'''


a="something went wrong"
a=a.split()
a="-".join(a)
print(a)
