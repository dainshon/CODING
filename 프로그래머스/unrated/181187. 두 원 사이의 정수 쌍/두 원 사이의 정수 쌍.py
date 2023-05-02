import math

def solution(r1, r2):
    answer = 0
    # a = counting(r2, 2)
    # b = counting(r1, 1)
    # print(a)
    # print(b)
    # answer = a-b+4

    for i in range(1, r2):
        if(i<r1):
            max = ((r2**2)-(i**2))**(1/2)
            min = ((r1**2)-(i**2))**(1/2)
            answer += math.floor(max)-math.ceil(min)+1

        else:
            answer+=math.floor(((r2**2)-(i**2))**(1/2))

    answer*=4
    answer += 4*(r2-r1+1)
    
        
        
        
    
    
    
    return answer


# def counting(r, n):
#     if(r==1):
#         return 5
#     add=0
#     count = 0
#     s_r = 0
#     for i in range(r-1, 0, -1):
#         if(2*(i**2) <= (r**2)):
#             s_r = i
#             break

#     count += (s_r**2)
#     for i in range(s_r+1, r):
#         num = (r**2)-(i**2)
#         num = num**(1/2)
#         int_num = int(num)   # 정수부분만 남기기
#         if(int_num == num and n==1): #   두 좌표가 모두 정수
#             add+=1
        
#         count += 2*int_num
    
#     count*=4
#     count = count +1+(4*r)
#     count += (8*add)    # 두 좌표 모두 정수인거 8배 더해줌(나중에 빼줄거니까): 2배는 대칭 4배는 4분면
    

    
#     return count