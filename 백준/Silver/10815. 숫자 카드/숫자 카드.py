N = int(input())
card = list(map(int, input().split()))

M = int(input())
check = list(map(int, input().split()))

result = []

#이진검색
card.sort()

for i in range(len(check)):  
  pl = 0
  pr = len(card)-1
  pc = (pr-pl)//2
  while(1):
    if(check[i] > card[len(card)-1] or check[i] < card[0]):
      result.append(0)
      break
    if(check[i]==card[pl] or check[i]==card[pc] or check[i]==card[pr]):
      result.append(1)
      break
    if (pc==pr or pc==pl):
      result.append(0)
      break
    if(check[i] > card[pc]):
      pl = pc
      pc = pc+(pr-pl)//2
    if(check[i] < card[pc]):
      pr = pc
      pc = pc-(pr-pl)//2
      
for i in range(len(result)):
  print(result[i], end=' ')
      