n=int(input('enter the limit:'))
a= list (map (int, input("enter the numbers: ").strip().split())) [:n]
socks_pair_c=0
unique_list=[]
for i in a:
    if i not in unique_list :
        unique_list.append(i)
print(unique_list)
for i in unique_list:
    c=0
    for j in a:
        if i==j:
            c+=1
    socks_pair_c+=c//2
print(socks_pair_c)

