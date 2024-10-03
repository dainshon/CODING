import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

cnt_forward = [-1] * (1001)
cnt_backward = [-1] * (1001)

cnt_list = []
for i in range(2):
    lst = [-1]*N
    cnt_list.append(lst)

# 앞에서부터 [][0]
for i in range(N):
    n = arr[i]
    if n==1:
        cnt_forward[n] = 0
        cnt_list[0][i] = 0
        continue
    cnt_forward[n] = max(cnt_forward[:n]) + 1
    cnt_list[0][i] = cnt_forward[n]

# 뒤에서부터 [][1]
for i in range(N-1,-1,-1):
    n = arr[i]
    if n==1:
        cnt_backward[n] = 0
        cnt_list[1][i] = 0
        continue
    cnt_backward[n] = max(cnt_backward[:n]) + 1
    cnt_list[1][i] = cnt_backward[n]

result = 0
for i in range(N):
    num = cnt_list[0][i]+cnt_list[1][i]
    result = max(result, num)
print(result+1)
