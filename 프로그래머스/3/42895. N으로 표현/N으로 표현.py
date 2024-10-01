def solution(N, number):
    answer = -1
    
    num_dict = {}
    num_dict[1] = [N]
    num_dict[2] = [10*N+N, N+N, N-N, N*N, N//N]
    if N == number:
        return 1
    for num in num_dict[2]:
        if num == number:
            return 2
    
    for i in range(3, 9):
        lst = []
        n_list = []
        for j in range(1,i//2+1):
            n_list.append((j,i-j))
        
      #  print()
        for (p,q) in n_list: #ㅜnum_dict[p]와 num_dict[q]에서 하나씩
           # print(p,q)
           # print(num_dict)
            for n1 in num_dict[p]:
                for n2 in num_dict[q]:
                   # print(n1,n2)
                    #사칙연산
                    for j in range(6):
                        if j==0:
                            num = n1+n2
                        elif j==1:
                            num = n1-n2
                        elif j==2:
                            num = n2-n1
                        elif j==3 and n2!=0:
                            num = n1//n2
                        elif j==4 and n1!=0:
                            num = n2//n1
                        elif j==5:
                            num = n1*n2
                            
                        if num == number:
                            return (i)
                        lst.append(num)
        num = 0
        for j in range(i):
            num += (10**j)*N
      #  print(num)
        if num == number:
            return(i)
        lst.append(num)
        num_dict[i] = lst
    return answer