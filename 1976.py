# 여행 가자 (Union Find)

def union(a: int, b: int) -> None:
    a = find(a)
    b = find(b)
    if a == b: # 이미 같은 집합에 있으면 NOP
        return
    
    # b를 a에 합침
    parents[a] = b

def find(a: int) -> int:
    if a == parents[a]:
        return a
    parents[a] = find(parents[a])
    return parents[a]

N = int(input())
M = int(input())

parents = [ i for i in range(N+1) ]
for i in range(1, N+1):
    temp_rel_lst = list(map(int, input().split()))
    for j in range(i, N):
        if temp_rel_lst[j] != 0:
            # parents[j+1] = i
            union(i, j+1)

target_path = list(map(int, input().split()))

## TEST
print(*parents)

OUTPUT = True
for i in range(M-1):
    if find(target_path[i]) != find(target_path[i+1]):
        OUTPUT = False
        break

if OUTPUT:
    print("YES")
else:
    print("NO")
