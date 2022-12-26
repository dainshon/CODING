import sys
T = int(sys.stdin.readline())

arr = [-1 for i in range(101)]

for i in range(1,6):
    if(i<=3):
        arr[i] = 1
    else:
        arr[i] = 2
max = 5
for i in range(T):
    N = int(sys.stdin.readline())
    if(N>max):
        for j in range(max+1, N+1):
            arr[j] = arr[j-1] + arr[j-5]
        max = N
        print(arr[N])
    else:
        print(arr[N])