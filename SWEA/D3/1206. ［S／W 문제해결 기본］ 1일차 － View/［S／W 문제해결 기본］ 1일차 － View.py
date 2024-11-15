
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.

for test_case in range(1, 11):
    N = int(input())
    heights = list(map(int, input().split()))

    result = 0
    for i in range(2,len(heights)-2):
        height = heights[i]
        max_height = 0
        for j in range(1,3):
            max_height = max(max_height, heights[i-j])
            max_height = max(max_height, heights[i+j])
        if(height > max_height):
            result += height-max_height
    print(f"#{test_case} {result}")
