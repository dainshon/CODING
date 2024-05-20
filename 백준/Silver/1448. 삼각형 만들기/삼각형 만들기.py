import sys

N = int(sys.stdin.readline())
arr = []
for i in range(N):
    arr.append(int(sys.stdin.readline()))
arr.sort()
answer = -1
for i in range(len(arr)-1, 1, -1):
    if arr[i-1]+arr[i-2] > arr[i]:
        answer = sum(arr[i-2:i+1])
        break
print(answer)