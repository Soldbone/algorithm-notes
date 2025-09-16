# 치킨 TOP N
import sys
input = sys.stdin.readline

# 입력
N = int(input())
chicken_lst = list(map(int, input().split()))
k = int(input())


# 코드
num_of_group = N // k

result = []
for i in range(num_of_group, len(chicken_lst)+1, num_of_group):
    result.extend(sorted(chicken_lst[i-num_of_group:i]))

# 출력
print(*result)
