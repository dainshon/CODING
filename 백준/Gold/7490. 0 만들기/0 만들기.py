import sys

stack = []
N = -1

def calculate(arr):
    global N
    num_list = []
    op_list = []
    # list들 셋팅
    num = "1"
    for i in range(N-1):
        if arr[i] != " ": # +, -면
            num_list.append(int(num))
            op_list.append(arr[i])
            num = str(i+2)
        else: # " "면
            num += str(i+2)

        if i>=N-2:
            num_list.append(int(num))
    # print(num_list)
    # print(op_list)

    # 계산
    total = num_list[0]
    for i in range(len(op_list)):
        if op_list[i] == '+':
            total += num_list[i+1]
        elif op_list[i] == '-':
            total -= num_list[i+1]

    if total == 0:
        for i in range(N-1):
            print((i+1), end="")
            print(arr[i], end="")
        print(N)


def back():
    global N
    if len(stack) == N-1:
        calculate(stack)
        return


    for s in [" ", "+", "-"]:
        stack.append(s)
        back()
        stack.pop()


K = int(sys.stdin.readline())
for i in range(K):
    N = int(sys.stdin.readline())
    back()
    print()