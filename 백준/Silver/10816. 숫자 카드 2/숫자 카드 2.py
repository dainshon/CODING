N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

dict = {}
for i in range(len(N_list)):
  if N_list[i] in dict.keys():
    value = dict[N_list[i]]
    dict[N_list[i]] = value+1
  else:
    dict[N_list[i]] = 1


for i in range(len(M_list)):
  if M_list[i] in dict.keys():
    print(dict[M_list[i]], end=' ')
  else:
    print('0', end=' ')