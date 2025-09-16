# 쉬운 계단 수
# https://cotak.tistory.com/12
# 풀이를 보면 이해가 되지만 이걸 혼자서 떠올리고 코드까지 짜는 것은 어려울 것 같다.
# 복습하자.

import sys
input = sys.stdin.readline

N = int(input())

dp = [[0]*10 for _ in range(N+1)]
for i in range(1, 10):
    dp[1][i] = 1

MOD = 1000000000

for i in range(2, N+1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[N]) % MOD)