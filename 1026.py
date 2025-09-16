# 보물

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

new_A = [ [A[x], x] for x in range(len(A)) ]
new_B = [ [B[x], x] for x in range(len(B)) ]

new_A.sort()
new_B.sort()


print(new_A)
print(new_B)

# S = 0
# for i in range(N):
#     S += A[i] * B[i]
# print(S)
