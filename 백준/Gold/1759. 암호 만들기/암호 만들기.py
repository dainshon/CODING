import sys
L, C = map(int, sys.stdin.readline().split())
arr = list(sys.stdin.readline().split())
arr.sort()
arr = [0] + arr
stack = []

def check_str(num_arr):
    cnt_m = 0
    cnt_j = 0
    for i in num_arr:
        if arr[i] in ['a','e','i','o','u']:
            cnt_m+=1
        else:
            cnt_j+=1
    if cnt_m>=1 and cnt_j>=2:
        return 1
    return 0

def change_to_str(num_arr):
    str = ""
    for i in num_arr:
        str+=arr[i]
    print(str)

def dfs(node):
    if len(stack)==L:
        # 모음자음 수 체크
        if check_str(stack):
            change_to_str(stack)
        return

    for n in range(node, C+1):
        stack.append(n)
        dfs(n+1)
        stack.pop()

dfs(1)
