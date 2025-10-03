# 사이클 게임 (유니온 파인드)
import sys
input = sys.stdin.readline

def union(a: int, b: int) -> None:
    a = find(a)
    b = find(b)
    if a == b:
        return
    
    if rank[a] > rank[b]:
        parents[b] = a
    elif rank[a] < rank[b]:
        parents[a] = b
    else:
        parents[b] = a
        rank[a] += 1


def find(a: int) -> int:
    if a == parents[a]:
        return a
    else:
        parents[a] = find(parents[a])
        return parents[a]


n, m = map(int, input().split())
parents = [ i for i in range(n) ]
rank = [ 0 for _ in range(n) ]
result = 0
for i in range(m):
    # point a, point b
    a, b = map(int, input().split())
    if find(a) == find(b): # find(a) == b or find(b) == a ## 틀렸던 코드
        result = i + 1
        break
    else:
        union(a, b)

print(result)
