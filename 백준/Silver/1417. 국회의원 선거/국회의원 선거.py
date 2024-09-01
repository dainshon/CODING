import sys
import heapq
from collections import deque

N = int(sys.stdin.readline())
h = []
arr = []
dasom = -1
for i in range(N):
    number = int(sys.stdin.readline())
    if i==0:
        dasom = number
        continue
    arr.append(number)
arr.sort(reverse=True)
dq = deque(arr)

result = 0

while(1):
    if len(dq)<=0:
        print(result)
        break

    n = dq.popleft()
    if n >= dasom:
        n -= 1
        for i in range(len(dq)+1):
            if i >= len(dq):
                dq.insert(i, n)
                dasom += 1
                result += 1
                break
            if dq[i] <= n:
                dq.insert(i, n)
                dasom += 1
                result += 1
                break

    else:
        print(result)
        break

