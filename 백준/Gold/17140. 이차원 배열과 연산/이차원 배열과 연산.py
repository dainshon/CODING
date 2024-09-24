import sys

r, c, k = map(int, sys.stdin.readline().split())
arr = []
for i in range(3):
    lst = list(map(int, sys.stdin.readline().split()))
    arr.append(lst)
# print(r,c,k)
# print(arr)

cnt = 0

def calculate_R(array):

    new_array = []
    max_length = 0
    for row in array:
        dict = {}
        for n in row:
            if n==0:
                continue

            if n in dict:
                dict[n] += 1
            else:
                dict[n] = 1
    # dictionary 값 기준 정렬법(오름차순)
        new_dict = sorted(dict.items(), key=lambda x: (x[1], x[0])) # x[1] 기준으로 정렬후 x[0]기준으로 정렬
        new_array.append(new_dict)
        max_length = max(max_length, len(new_dict))

    # 최대 크기 맞춰서 재정렬
    for i in range(len(new_array)):
        row = new_array[i]
        lst = []
        for (a, b) in row:
            lst.append(a)
            lst.append(b)
        if len(row) < max_length:
            zero_list = [0]*(2*(max_length-len(row)))
            lst = lst + zero_list
        new_array[i] = lst
    return new_array

def reverse_array(array):
    reverse_array = []
    for j in range(len(array[0])):
        lst = []
        for i in range(len(array)):
            lst.append(array[i][j])
        reverse_array.append(lst)
    return reverse_array


def calculate_C(array):
    new_array = reverse_array(array)
    # R연산
    new_array = calculate_R(new_array)
    # 결과 다시 row-column 바꿈
    new_array = reverse_array(new_array)
    return new_array


while(1):
    if r-1<len(arr) and c-1<len(arr[0]) and arr[r-1][c-1] == k:
        break

    if cnt > 100:
        cnt = -1
        break
    cnt_r = len(arr)
    cnt_c = len(arr[0])

    if cnt_r >= cnt_c:
        arr = calculate_R(arr)
    else:
        arr = calculate_C(arr)

    cnt += 1

    # 100 넘는지 췍
    if len(arr)>=100:
        for i in range(100, len(arr)):
            del arr[i]
    if len(arr[0]) >= 100:
        for i in range(len(arr)):
            arr[i] = arr[i][0:100]

print(cnt)


