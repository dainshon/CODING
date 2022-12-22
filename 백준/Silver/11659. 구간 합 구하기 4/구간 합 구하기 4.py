import sys

# readline은 한줄만 입력받고
# readlines는 여러줄 입력받아서 한 줄씩 리스트에 원소로 들어감

N, M = map(int,sys.stdin.readline().split())
list = list(map(int,sys.stdin.readline().split()))

#누적합을 아예 배열로 만들어버림 (prefix)
prefix = []
prefix.append(0)

for i in range(N):
    prefix.append(prefix[i]+list[i])



for k in range(M):
    i, j = map(int,sys.stdin.readline().split())
    print(prefix[j]-prefix[i-1])

