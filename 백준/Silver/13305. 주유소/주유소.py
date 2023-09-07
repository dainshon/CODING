N = int(input())
dis = list(map(int, input().split()))
price = list(map(int, input().split()))
min_price = 100000
index_p = 0
for i in range(N):
  if(min_price > price[i]):
    min_price = price[i]
    index_p = i
    
result = 0
while(1):

  for i in range(index_p,N-1):
    result += (dis[i]*min_price)
    dis[i] = 0
  min_price = 100000
  for i in range(0, index_p):
    if(min_price > price[i]):
      min_price = price[i]
      index_p = i
  if(dis[0]==0):
    break
print(result)