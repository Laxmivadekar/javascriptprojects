# my_list = [-15, -26, 15, 1, 23, -64, 23, 76]
# new_list = []

# while my_list:
#     min = my_list[0]  
#     for x in my_list: 
#         if x >min:
#             min = x
#     new_list.append(min)
#     my_list.remove(min)    

# print(new_list)

a=[]
k=1
while k<=3:
    n=int(input("enter any number: "))
    a.append(n)
    k+=1
i=0
max=a[i]
while i<len(a):
    if a[i]>max:
        max=a[i]
    i+=1
print(max)