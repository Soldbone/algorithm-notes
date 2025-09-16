# 1, 2, 3 더하기

# 입력
import sys
input = sys.stdin.readline

dp = [0] * 11

# initialize
dp[1] = 1
dp[2] = 2
dp[3] = 4

# bottom-up DP
for i in range(4, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for _ in range(int(input())):
    target = int(input())
    print(dp[target])
