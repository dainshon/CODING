N = int(input())
dict_x = {}
dict_y = {}

for i in range(N):
    a, b = map(int, input().split())
    dict_x[i] = a
    dict_y[i] = b

sort_dict_x = sorted(dict_x.items(), key = lambda item: item[1])

p=0
q=1
while(1):

    while(1):
        if(q>=N):
            break
        elif(sort_dict_x[p][1] == sort_dict_x[q][1]):
            q+=1
        else:
            break

    new_list = []
    
    for i in range(p,q):
        index = sort_dict_x[i][0]
        new_list.append(dict_y[index])
    new_list.sort()

    for y in new_list:
        print(sort_dict_x[p][1], y)
        
    if(q>=N):
        break

    p = q
    q = p+1