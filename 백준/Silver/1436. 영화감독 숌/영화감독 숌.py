cnt = int(input())

num = 666
rank = 0
while(1):
  num_list = list(map(int, str(num)))
  length = len(str(num))
  for i in range(length):
    if(i <= length-3 and num_list[i] == 6):
      if(num_list[i+1] == 6 and num_list[i+2] == 6):
        rank+=1
        break
  if(rank == cnt):
    print(num)
    break
  num+=1