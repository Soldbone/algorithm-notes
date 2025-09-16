# 색종이 만들기
n = int(input())

paper_lst = []
for _ in range(n):
    paper_lst.append(list(map(int, input().split())))

white, blue = 0, 0

def check_and_count_paper(n, i, j):
    global white
    global blue
    IS_WHITE = True
    IS_BLUE = True
    for row in range(i, i+n):
        if paper_lst[row][j:j+n] != [0] * n:
            IS_WHITE = False
        if paper_lst[row][j:j+n] != [1] * n:
            IS_BLUE = False

    if IS_WHITE:
        white += 1
        return True
    if IS_BLUE:
        blue += 1
        return True
    
    return False

def rec_divide_paper(n, i, j):
    if check_and_count_paper(n, i, j):
        return True
    else:
        n //= 2
        return rec_divide_paper(n, i, j), rec_divide_paper(n, i+n, j), rec_divide_paper(n, i, n+j), rec_divide_paper(n, i+n, n+j)
    
rec_divide_paper(n, 0, 0)
print(white, blue, sep='\n')