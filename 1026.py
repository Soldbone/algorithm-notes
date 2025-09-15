# 보물

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

S = 0
for i in range(N):
    S += A[i] * B[i]
print(S)

# amado님 코드
a = int(input())
A = sorted(map(int, input().split()), )
B = sorted(map(int, input().split()), reverse=True)
sum = 0
for i in range(a):
    sum += A[i]*B[i]
print(sum)
