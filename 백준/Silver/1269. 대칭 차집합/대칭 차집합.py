#list = list(map(int, input().split()))
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#list를 dictionary로
A_dict = dict.fromkeys(A,0)

dup_cnt = 0

for i in range(M):
  if B[i] in A_dict:
    dup_cnt += 1

print(N+M-(2*dup_cnt))