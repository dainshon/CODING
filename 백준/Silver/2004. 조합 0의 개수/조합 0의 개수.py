import sys
N, M = map(int,sys.stdin.readline().split())

#시간초과 -> 하나하나 세는방법말고 한번에 퉁쳐서 세는방법

# num! 2 갯수
def count_two(num):
    count = 0
    square = 1
    while(num//(pow(2,square))!=0):
        count += num//pow(2, square)
        square+=1
    return count

# num! 5 갯수
def count_five(num):
    count = 0
    square = 1
    while(num//(pow(5,square))!=0):
        count += num//pow(5, square)
        square+=1
    return count

two = count_two(N) - (count_two(M)+count_two(N-M))
five = count_five(N) - (count_five(M)+count_five(N-M))

if(two>0 and five>0):
    print(min(two, five))
else:
    print('0')