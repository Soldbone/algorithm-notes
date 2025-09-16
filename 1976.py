# 여행 가자
import sys
input = sys.stdin.readline


N = int(input())
M = int(input())

parent = [ i for i in range(N+1) ]


'''
a와 b를 합친다.
int, int -> void
'''
def union(a: int, b: int):
    a = parent[a]
    b = parent[b]
    if a == b:
        return
    parent[b] = a


'''
a의 부모를 찾는다.
int -> int
'''
def find(a: int):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]

for i in range(1, N+1):
    input_line = list(map(int, input().split()))
    for j in range(i, N):
        if input_line[i] == 1:
            # parent[j+1] = i
            union(i, j+1)

target_path = list(map(int, input().split()))
for i in range(N-1):
    if find(target_path[i]) != find(target_path[i+1]):
        print("NO")
        break
else:
    print("YES")
    