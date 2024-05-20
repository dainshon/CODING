import sys
A, B = map(int, sys.stdin.readline().split())
cnt = 0
while(1):
    if B % 2 == 0:
        B = B//2
        cnt += 1
    elif B%10 == 1:
        B = B//10
        cnt += 1
    else:
        print(-1)
        break

    if B < A :
        print(-1)
        break

    if A == B:
        print(cnt+1)
        break
