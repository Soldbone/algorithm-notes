# # 적록색약
# # [REF] https://velog.io/@nyc326/Python-백준-10026번-적록색약-BFS

# import sys
# from collections import deque
# input = sys.stdin.readline

# # BFS 함수 정의
# def bfs(graph, start, visited):
#     queue = deque([start])
#     x, y = start
#     visited[x][y] = 1

#     directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#     while queue:
#         x, y = queue.popleft()
        
#         curr_value = graph[x][y]
#         for dx, dy in directions:
#             nx, ny = x + dx, y + dy
#             if ( (0 <= nx < N) and (0 <= ny < N) ) and (graph[nx][ny] == curr_value) and not visited[nx][ny]:
#                 queue.append((nx, ny))
#                 visited[nx][ny] = 1

# N = int(input().rstrip())
# graph = [ list(input()) for _ in range(N) ]

# visited = [ [0] * N for _ in range(N) ]
# non_blind_count, rg_blind_count = 0, 0

# # Non Color Blind
# for i in range(N):
#     for j in range(N):
#         if not visited[i][j]:
#             bfs(graph, (i, j), visited)
#             non_blind_count += 1

# # RG Color Blind
# for i in range(N):
#     for j in range(N):
#         if graph[i][j] == "R":
#             graph[i][j] = "G"

# visited = [ [0] * N for _ in range(N) ]
# for i in range(N):
#     for j in range(N):
#         if not visited[i][j]:
#             bfs(graph, (i, j), visited)
#             rg_blind_count += 1

# print(non_blind_count, rg_blind_count)


# 적록색약
# [REF] good1588님 풀이

import sys
input = sys.stdin.readline

def dfs(color, x, y):
    stk = [(x,y)]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while stk:
        x, y = stk.pop()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if ( 0 <= nx < N and 0 <= ny < N ) and (graph[nx][ny] == color):
                stk.append((nx, ny))
                visited[nx][ny] = 1

# Input
N = int(input().rstrip())
graph = [ list(input()) for _ in range(N) ]

visited = [ [0] * N for _ in range(N) ]
non_blind_count, rg_blind_count = 0, 0

# Non Color Blind
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(graph, (i, j), visited)
            non_blind_count += 1

# RG Color Blind
for i in range(N):
    for j in range(N):
        if graph[i][j] == "R":
            graph[i][j] = "G"

visited = [ [0] * N for _ in range(N) ]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            dfs(graph, (i, j), visited)
            rg_blind_count += 1

# Output
print(non_blind_count, rg_blind_count)
