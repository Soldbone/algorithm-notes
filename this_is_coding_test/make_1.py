# 1로 만들기
# [조건] 1 <= X <= 30,000
# 5로 나누기 / 3으로 나누기 / 2로 나누기 / 1 빼기

X = int(input())

dp = [0] * 30001

for i in range(2, X + 1):
    # 1 빼는 경우
    dp[i] = dp[i - 1] + 1
    # 2로 나누어 떨어지는 경우
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)
print(dp[X])
