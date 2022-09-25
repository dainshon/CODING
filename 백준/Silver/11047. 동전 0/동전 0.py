N, K = map(int, input().split())
money=[]
for i in range(N):
  money.append(int(input()))
cnt = 0

while(1):
  for i in range(N-1, -1, -1):
    if(money[i]<=K):
      cnt += K//money[i]
      K -= money[i]*(K//money[i])
      break
  if(K==0):
    break

print(cnt)
