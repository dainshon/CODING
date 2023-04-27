def solution(targets):
    answer = 0
    i = 1
    j = -1
    dic_list = []
    
    for target in targets:
        # 시작
        lst = []
        lst.append(target[0])
        lst.append(i)
        # 끝
        lst_2 = []
        lst_2.append(target[1])
        lst_2.append(j)
        
        i+=1
        j-=1
        dic_list.append(lst)
        dic_list.append(lst_2)

    dic_list.sort(key=lambda x:(x[0],x[1]))

    dic = {}
    n = 0
    for lst in dic_list:
        dic[lst[1]] = n
        n+=1
    stack = []
    for lst in dic_list:
        if(lst[1]>0):
            stack.append(lst[1])
        elif(lst[1]<0):
            while(len(stack)>0):
                num = -stack.pop()
                dic_list[dic[num]][1] = 0    #   리스트에서 몇번째에 있는지
            answer+=1

    
    return answer