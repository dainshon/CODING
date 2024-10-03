import copy

N = int(input())

graph = [[1,2,3],[2,3],[1,3],[1,2]]
stack = []

def check_good_array(arr): # 좋은 수열인지 체크
    arr_len = len(arr)
    for g_len in range(2,arr_len//2+1):
        flag = 0
        for n in range(g_len):
            if arr[-(2*g_len)+n] != arr[-g_len+n]:
                flag = 1
                break
        if flag == 0: # g_len 개의 수열이 같다
            return 0
    return 1

finish = 0
def back(node):
    global finish
    if len(stack)==N:
     #   print(stack)
        answer = ""
        for s in stack:
            answer += str(s)
        print(answer)
        finish = 1
        return

    for n in graph[node]:
        # 좋은 수열인지 체크
        stack.append(n)
        if len(stack)>=3:
            if not check_good_array(stack):
               #print("나쁨: ", stack)
                stack.pop()
                continue
        back(n)
        stack.pop()
        if finish == 1:
            return

back(0)
