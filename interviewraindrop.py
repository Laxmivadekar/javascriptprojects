# class Solution:
#     # @param A : tuple of integers
#     # @return an integer
#     def trap(A):
#         left_max, right_max=0, 0
#         l=0
#         h=len(A)-1
#         water=0
#         while(l<=h):
#             if A[l]<A[h]:
#                 if A[l]>left_max:
#                     left_max=A[l]
#                 else:
#                     water+=left_max-A[l]
#                 l+=1
#             else:
#                 if A[h]>right_max:
#                     right_max=A[h]
#                 else:
#                     water+=right_max-A[h]
#                 h-=1
#         return water
#     A=[1,2]
#     print(trap(A))
                

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        pA = 0
        pB = 0
        pC = 0
        minmax = float("inf")
        while pA < len(A) and pB < len(B) and pC < len(C):
            minmax = min(minmax, max(abs(A[pA] - B[pB]), abs(B[pB] - C[pC]), abs(C[pC] - A[pA])))
            if A[pA] == min(A[pA], B[pB], C[pC]):
                pA += 1
            elif B[pB] == min(A[pA], B[pB], C[pC]):
                pB += 1
            else:
                pC += 1
        
        return minmax


