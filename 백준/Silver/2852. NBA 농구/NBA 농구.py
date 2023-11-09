N = int(input())

score = [0,0]

winning_time_1 = []
winning_time_2 = []

winning_team = -1
lst = []
for i in range(N):
  team, time = input().split()
  team = int(team)
  score[team-1]+=1

  # if(i==N-1):
  #   if(score[0]!=score[1]):
  #     lst.append()
    
  #   lst.append("48:00")
  #   if(winning_team==1):
  #     winning_time_1.append(lst)
  #   elif(winning_team==2):
  #     winning_time_2.append(lst)
  #   break

  if(score[0]>score[1]): # 1팀이 이기고있음
    if(winning_team!=1):
      winning_team = 1
      lst.append(time)  # 시작
  elif(score[0]<score[1]): # 2팀이 이기고있음
    if(winning_team!=2):
      winning_team = 2
      lst.append(time) # 시작 
  else: # 비김
    lst.append(time)
    if(winning_team==1):
      winning_time_1.append(lst)
    else:
      winning_time_2.append(lst)
    lst = []
    winning_team = -1

if(winning_team != -1):
  lst.append('48:00')
  if(winning_team==1):
    winning_time_1.append(lst)
  else:
    winning_time_2.append(lst)

def calc_time(winning_time):
  total_h = 0
  total_m = 0
  # 시간 계산
  for t in winning_time:
    s_h, s_m = map(int, t[0].split(':'))
    e_h, e_m = map(int, t[1].split(':'))
    f_h = e_h - s_h
    f_m = e_m - s_m

    if(f_m < 0):
      f_h-=1
      f_m+=60
    total_h += f_h
    total_m += f_m


  if(total_m>=60):
    total_h += (total_m//60)
    total_m = total_m%60
  
    
  total_h_str = str(total_h)
  total_m_str = str(total_m)
  
  if(total_h<10):
    total_h_str = '0' + total_h_str
  if(total_m<10):
    total_m_str = '0' + total_m_str

  print(total_h_str+':'+total_m_str)


calc_time(winning_time_1)
calc_time(winning_time_2)


    
