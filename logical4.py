'''import math
import os
import random
import re
import sys
def compareTriplets(a, b):
    alice_c=0
    bob_c=0
    for i in range(0,len(a)):
        if a[i]==b[i]:
            pass
        elif a[i]>b[i]:
            alice_c+=1
        elif a[i]<b[i]:
            bob_c+=1
    return [ alice_c,bob_c]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(result)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()'''

def compareTriplets(a, b):
    alice_c=0
    bob_c=0
    for i in range(0,len(a)):
        if a[i]==b[i]:
            pass
        elif a[i]>b[i]:
            alice_c+=1
        elif a[i]<b[i]:
            bob_c+=1
    return [ alice_c,bob_c]
a = list(map(int, input("enter the list1: ").rstrip().split()))
b = list(map(int, input("enter the list2: ").rstrip().split()))
result = compareTriplets(a, b)
print(result)