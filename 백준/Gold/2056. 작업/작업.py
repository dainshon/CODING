import sys
N = int(sys.stdin.readline())

task_finish_info = {} # key: 각 테스크 value: 끝나는 시간
task_into = {} # key: 각 테스크 value: [시간, 갯수, 정보]

for i in range(1,N+1):
    task_finish_info[i] = -1  # 끝
    lst = list(map(int, sys.stdin.readline().split()))
    task_into[i] = lst

while(1):
    # 모든 task_finish_info -1 아니면 종료
    flag = 1
    for i in range(1,N+1):
        if task_finish_info[i]==-1:
            flag = 0
            break
    if flag == 1:
        print(max(task_finish_info.values()))
        break


    for i in range(1,N+1):
        if task_into[i][1] == 0:
            task_finish_info[i] = task_into[i][0]
            continue
        if task_finish_info[i] != -1:
            continue

        # 선행들 시간 -1 아닌거 확인
        pretask_finish_max = -1
        for pretask in task_into[i][2:]:
            if task_finish_info[pretask] == -1:
                pretask_finish_max = -1
                break
            else:
                pretask_finish_max = max(pretask_finish_max, task_finish_info[pretask])
        if pretask_finish_max!=-1:
            task_finish_info[i] = pretask_finish_max+task_into[i][0]




