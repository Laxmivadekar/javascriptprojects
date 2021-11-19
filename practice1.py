# 177
# 10
'''a=int(input())
b=int(input())
t=()
c=a//b
d=a%b
print((c,d))'''

# for i in range(1,int(input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
#     print (pow(int(pow(10,i)/9),2))
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print( format(sum(student_marks[query_name])/len(student_marks[query_name]), ".2f") )
