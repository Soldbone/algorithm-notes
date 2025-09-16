# 효율적인 화폐 구성
# [조건] 서로 다른 N가지 종류의 화폐의 개수를 최소한으로 하여 M원을 만든다.
# 예시) 2원, 3원이 있을 경우 15원을 만들 때 3원 5개를 사용하는 것이 최솟값이다.
# 1 <= N <= 100, 1 <= M <= 10,000
# 
# 입력 예시)
# 2 15
# 2
# 3

n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])