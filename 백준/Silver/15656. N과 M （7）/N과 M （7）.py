import sys
sys.setrecursionlimit(10**6)

N, M = map(int,input().split())

num_list = list(map(int,input().split()))
num_list.sort()


def dfs():
  if(len(lst)==M):
    
    if(M==1):
      for n in num_list:
        print(n)
      return

    show(lst)
    if(sum(lst)>=M*(N-1)):
      return
    if(lst[-1]<N-1):
      lst[-1]+=1
    else:
  
      while(lst[-1]>=N-1):
        lst.pop()
      lst[-1]+=1
    dfs()

  else:
    lst.append(0)
    dfs()

def show(lst_):
  for n in lst_:
    print(num_list[n], end=' ')
  print()

lst = []
num = 0
dfs()