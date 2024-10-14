import sys
import math
N = int(sys.stdin.readline())

stack = []
def is_prime(num):

    for n in range(2,(int(math.sqrt(num))+1)):
        if num%n == 0:
            return 0  # 나눠짐. 소수아님
    return 1 # 안나눠짐 소수임


def back(num):
    num_str = ""
    for n in stack:
        num_str += str(n)
    if not is_prime(int(num_str)):
        return
    if len(stack)==N:
        print(num_str)
        return

    for n in [1,3,7,9]:
        stack.append(n)
        back(n)
        stack.pop()


for i in [2,3,5,7]:
    stack = []
    stack.append(i)
    back(i)
