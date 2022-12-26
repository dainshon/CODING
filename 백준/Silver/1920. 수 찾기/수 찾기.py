import sys

dict = {}
N = int(sys.stdin.readline())
A = list(map(int,sys.stdin.readline().split()))
for a in A:
    dict[a] = 1
M = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
for num in arr:
    if(num in dict):
        print('1')
    else:
        print('0')