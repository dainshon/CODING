K = int(input())
direction=[]
length=[]
hor = []
ver = []
for i in range(6):
  D , L = map(int, input().split())
  direction.append(D)
  length.append(L)
  if(D==1 or D==2):
    hor.append(L)
  else:
    ver.append(L)

index_a=-1
index_b=-1

for i in range(5):
  if(direction[i]==1 and direction[i+1]==3):
    index_a = i
    index_b = i+1
    break
  elif(direction[i]==2 and direction[i+1]==4):
    index_a = i
    index_b = i+1
    break
  elif(direction[i]==3 and direction[i+1]==2):
    index_a = i
    index_b = i+1
    break
  elif(direction[i]==4 and direction[i+1]==1):
    index_a = i
    index_b = i+1
    break
  else:
    index_a = 0
    index_b = 5

ver_max = max(ver)
hor_max = max(hor)

bigsize = ver_max*hor_max
smallsize = length[index_a]*length[index_b]

total_size = bigsize-smallsize

print(total_size*K)

    