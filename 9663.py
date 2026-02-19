# [Unsolved]

def promising(i, n, col):
    is_promising = True
    k = 1
    while (k<i and is_promising):
        # 대각선에 위치하거나 같은 열에 있는 경우
        if (col[i] == col[k] or abs(col[i]-col[k]) == i-k):
            is_promising = False
        k += 1

    return is_promising

count = 0
def nqueens(i, n, col: list):
    if promising(i, n, col):
        if i == n:
            global count
            count += 1
        else:
            for j in range(1, n+1):
                col[i+1] = j
                nqueens(i+1, n, col)


N = int(input())
col = [0]*(N+1)
nqueens(0, N, col)
print(count)
