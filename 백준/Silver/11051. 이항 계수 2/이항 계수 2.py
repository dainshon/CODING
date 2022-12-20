import sys

N, K = map(int,sys.stdin.readline().split())
if(K>(N//2)):
    K = N-K

up = 1
down = 1

for i in range(K):
    up *= (N-i)
    down *= (K-i)

print((up//down)%10007)