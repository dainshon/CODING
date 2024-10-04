import sys
N, M, K = map(int, sys.stdin.readline().split())
fire_balls = []
arr = []
for i in range(N+1):
    lst = [0] * (N+1)
    arr.append(lst)

# r,c,m,s,d
# 초기 fireball 받음
for i in range(M):
    lst = list(map(int, sys.stdin.readline().split()))
    fire_balls.append(lst)

dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
def move(fire_balls):
    new_fireball_dict = {}
    new_fireball_list = []
    for fire_ball in fire_balls:
        r, c, m, s, d = fire_ball[0],fire_ball[1],fire_ball[2],fire_ball[3],fire_ball[4]


        # 이동
        nx = r + (s%N)*dx[d]
        ny = c + (s%N)*dy[d]

        if nx<1:
            nx += N
        elif nx>N:
            nx -= N

        if ny<1:
            ny += N
        elif ny > N:
            ny -= N

        if (nx,ny) not in new_fireball_dict:
            new_fireball_dict[(nx,ny)] = [[m,s,d]]
        else:
            new_fireball_dict[(nx,ny)].append([m,s,d])
    # new_fireball_dict 만들기 끝

    # 겹치는거 있는지 확인 & 처리해서 새로운 fire_ball 만듦
    for k, v in new_fireball_dict.items():
        if len(v)==1:
            lst = list(k) + v[0]
            new_fireball_list.append(lst)
        else:  # 여러개
           # print("여러개임")
            # 방향 홀짝 구분
            sum_m = 0
            sum_s = 0
            odd_even = 0
            for ball in v:
                sum_m += ball[0]
                sum_s += ball[1]
                odd_even += ball[2]%2

            new_m = sum_m//5
            new_s = sum_s//len(v)
            if new_m==0:
                continue

            if odd_even==0 or odd_even==len(v): # 모두 짝수 or 홀수
                for new_d in [0,2,4,6]:
                    lst = list(k) + [new_m,new_s,new_d]
                    new_fireball_list.append(lst)
            else:
                for new_d in [1,3,5,7]:
                    lst = list(k) + [new_m,new_s,new_d]
                    new_fireball_list.append(lst)

    return new_fireball_list


for i in range(K):
    fire_balls = move(fire_balls)


result = 0
for fire_ball in fire_balls:
    result += fire_ball[2]
print(result)