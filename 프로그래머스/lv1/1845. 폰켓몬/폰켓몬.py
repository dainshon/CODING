def solution(nums):
    cnt = len(nums)//2
    arr = []
    
    answer = 0
    for i in range(len(nums)):
        flag = 0
        for j in range(len(arr)):
            if(arr[j] == nums[i]):
                flag = 1
                break
        if(flag == 0):
            arr.append(nums[i])
            
    if(len(arr)>=cnt):
        answer = cnt
    else:
        answer = len(arr)
    
    return answer