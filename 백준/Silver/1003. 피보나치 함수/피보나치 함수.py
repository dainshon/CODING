import sys
T = int(sys.stdin.readline())

zero = 0
one = 0

zero_dict = {}
one_dict = {}

fib_list = [0,1]
zero_dict[0] = 1
zero_dict[1] = 0
one_dict[0] = 0
one_dict[1] = 1




def fibonacci(num):
    global zero
    global one
    if(num in fib_list):
        zero += zero_dict[num]
        one += one_dict[num]
        return 0
    elif(num-1 in fib_list and num-2 in fib_list):
        fib_list.append(num)
        zero_dict[num] = zero_dict[num-1] + zero_dict[num-2]
        one_dict[num] = one_dict[num-1] + one_dict[num-2]
        zero += zero_dict[num]
        one += one_dict[num]
        return 0
    else:
        return fibonacci(num-1)+fibonacci(num-2)

for i in range(T):
    zero = 0
    one = 0
    N = int(sys.stdin.readline())
    fibonacci(N)
    print(zero, one)
