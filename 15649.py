# N과 M (1)

# 내 힘으로 못 풀어서 포기
# https://jie0025.tistory.com/455

def backtracking():
    if len(array) == m:
        print(" ".join(map(str, array)))
        return

    for i in range(1, n+1):
        if i not in array:
            array.append(i)
            backtracking()
            array.pop()

n, m = map(int,input().split())
array = []

backtracking()
