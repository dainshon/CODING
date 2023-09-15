
def recur():
  global N
  global result
  
  if(len(lst)==0):
    return

  elif(len(lst)==3):
    # 계산
    n = sum(lst)
    num = 1
    for i in range(3):
      r = lst[i]
      if(r!=0):
        num *= combination(n,r)
        n -= r
    result+=num
      
    lst.pop()
    recur()
  elif(lst[-1]==0):
    lst.pop()
    recur()
  # 2 줄이기
  elif(len(lst)==2):
    lst[1]-=1
    lst.append(N-(3*lst[0])-(2*lst[1]))
    recur()
  # 1 줄이기
  elif(len(lst)==1):
    lst[0]-=1
    lst.append((N-(3*lst[0]))//2)
    lst.append(N-(3*lst[0])-(2*lst[1]))
    recur()


def combination(n,r):
  p = 1
  q = 1
  if(r>n//2):
    r = n-r
  for i in range(r):
    q*=(n-i)
  for i in range(2,r+1):
    p*=i
  return q/p

T = int(input())
lst = []
num_list = []
global result
result = 0


for i in range(T):
  global N
  result=0
  N = int(input())
  lst = []
  lst.append(N//3)
  lst.append(N%3//2)
  lst.append(N%3%2)

  recur()
  print(int(result))
  
  