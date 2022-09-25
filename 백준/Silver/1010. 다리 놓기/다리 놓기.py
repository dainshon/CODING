def Combination(n,m):
  A = 1
  B = 1
  for i in range(n):
    A*=m
    m-=1
    B*=n
    n-=1
  
    
  return A//B

T = int(input())
for i in range(T):
  N, M = map(int, input().split())
  print(Combination(N,M))