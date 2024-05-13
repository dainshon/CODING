def solution(number, k):
    answer = []
    answer_len = len(list(number)) - k

    result_list = []
    last_idx = -1
    
    for num in number:
        
        while(1):
            if k>0 and answer and answer[-1]<num:
                answer.pop()
                k-=1
                continue
            else:
                break
        if len(answer) < answer_len:
            answer.append(num)
    

     # 결과 만들기
    for s in result_list:
        answer += s
                         

    
    return "".join(answer)