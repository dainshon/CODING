import sys
sys.setrecursionlimit(10**5)

s_list = []
skip_list = []

def solution(s, skip, index):
    answer = ''
    
    global s_list
    global skip_list
    
    for char in list(s):
        s_list.append(ord(char))    # 문자 -> 아스키코드
    
    for char in list(set(skip)):
        skip_list.append(ord(char))
        
    skip_list.sort()
    
    
    for number in s_list:
        print()
        start = number
        end = number + index
        add_number = 0
        while(1):
            if(end > 122):
                end -= 26
            if(start > 122):
                start -= 26
            
            result = count(start, end)
            add_number += result
            if(result == 0):
                break
            
            start = end + 1
            end = start+result-1
        
        result = number + index + add_number

        while(1):   #  26보다 훨씬 더 넘어가는 경우 있을 수 있음
            if(result<=122):
                break
            else:
                result -= 26

        answer += chr(result)
               
    return answer


def count(start, end):
    number = 0
    length = len(skip_list)
    print(start, end)
    if(start > end):
        for i in range(length-1,-1,-1):
            if(skip_list[i]>=start):
                number+=1
            elif(skip_list[i]<start):
                break
        for i in range(length):
            if(skip_list[i]<=end):
                number+=1
            elif(skip_list[i]>end):
                break
    else:
        for i in range(length):
            if(skip_list[i]>=start and skip_list[i]<=end):
                number+=1
            elif(skip_list[i] > end):
                break
    return number
    