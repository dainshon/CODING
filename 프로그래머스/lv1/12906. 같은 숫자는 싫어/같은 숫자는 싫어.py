def solution(arr):
    answer = [-1]
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    for i in range(len(arr)):
        if(arr[i] != answer[-1]):
            answer.append(arr[i])
    answer.remove(-1)
    return answer