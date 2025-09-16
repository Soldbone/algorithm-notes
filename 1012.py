# 유기농 배추
# 이번에도 풀이를 보긴 했지만 내 아이디어로 구현했다.

import sys
input = sys.stdin.readline

# 1697(숨바꼭질)에서 사용했던 bfs 코드 참고함
def bfs(napa_cabbage_coord: set):
    # Respectively, up/right/down/left
    # dx = [0, 1, 0, -1]
    # dy = [1, 0, -1, 0]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    s = [napa_cabbage_coord.pop()]
    while s:
        x, y = s.pop()
    
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if (nx, ny) in napa_cabbage_coord:
                s.append((nx, ny))
                napa_cabbage_coord.discard((nx, ny))

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    napa_cabbage_coord = { tuple(map(int, input().split())) for _ in range(K) }

    count = 0
    for i in range(K):
        if len(napa_cabbage_coord):
            bfs(napa_cabbage_coord)
            count += 1
        else:
            break

    print(count)
