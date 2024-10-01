from collections import deque

def solution(n, computers):
    answer = 0
    graph = []
    visited = [False]*n
    for i in range(n):
        lst = []
        for j in range(n):
            if i!=j and computers[i][j]==1:
                lst.append(j)
        graph.append(lst)
    # print(graph)
    # print(visited)
    
    for i in range(n):
        if visited[i]==True:
            continue
        
        dq = deque()
        dq.append(i)

        # 연결된거 구하기

        while(1):

            if len(dq)==0:
                break
            num = dq.popleft()
            visited[num] = True

            for number in graph[num]:

                if visited[number] == False:
                    dq.append(number)


        answer+=1

    
    return answer