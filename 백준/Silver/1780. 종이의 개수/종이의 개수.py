N = int(input())
paper = []

result = {-1:0, 0:0, 1:0}

def check(n, lst = []):  # 다 같은지 쳌, 길이
  flag = 0

  for i in range(n):
    for j in range(n):
      if(lst[i][j]!=lst[0][0]):
        flag = 1
        break
    if(flag==1):
      break

  if(flag==0):
    result[lst[0][0]]+=1  
    return
  
  # 9분할해서 다시 재귀

    
  if(flag==1):
    for i in range(0, n, n//3):
      for j in range(0, n, n//3):
        new_list = []
        for k in range(i, i+(n//3)):
          new_list.append(lst[k][j:j+(n//3)])
        check(len(new_list), new_list)

    

for i in range(N):
  lst = list(map(int, input().split()))
  paper.append(lst)

check(len(paper),paper)

print(result[-1])
print(result[0])
print(result[1])