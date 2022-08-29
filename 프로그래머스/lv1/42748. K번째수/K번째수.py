def solution(array, commands):
   # print(len(commands[2]))
    answer = []
    for p in range(len(commands)):
        arr = []
        
        i = commands[p][0]
        j = commands[p][1]
        k = commands[p][2]
        
        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[k-1])
        
    return answer