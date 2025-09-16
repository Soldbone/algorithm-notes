# 숨바꼭질
# https://chancoding.tistory.com/193
# https://wook-2124.tistory.com/273
# 문제를 내 힘으로 풀지 못하고 있다. 코드를 잘 이해하고 복습하자.

import sys
from collections import deque

input = sys.stdin.readline

'''
N에서 K에 도달할 때까지 무한 반복. 도달 시 반환.
visited 역할을 하는 'array' 리스트 존재. (문제에 제시된 입력 범위로 array 크기 결정)
이미 array에 값이 존재한다면 더 적은 횟수로 해당 수에 도달할 수 있는 것이므로 update 안 함.
tuple 형태로 iteration한다는 발상을 못 했음.
'''
def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return array[v]
        for next_v in (v-1, v+1, 2*v):
            if 0 <= next_v < MAX and not array[next_v]:
                array[next_v] = array[v] + 1
                q.append(next_v)

MAX = 100001
n, k = map(int, input().split())
array = [0] * MAX
print(bfs(n))
