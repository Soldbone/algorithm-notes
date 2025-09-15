# 쿼드트리 (답 보고 풀음)

## 입력
import sys
input = sys.stdin.readline
N = int(input())
image = [ list(map(int, input().rstrip())) for _ in range(N) ]

result = []
def quad_tree(x,y,n):
    global result
    color = image[x][y]

    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != image[i][j]:
                result.append("(")
                quad_tree(x,y,n//2)
                quad_tree(x, y+n//2, n//2)
                quad_tree(x+n//2, y, n//2)
                quad_tree(x+n//2, y+n//2, n//2)
                result.append(")")
                return
    result.append(color)

quad_tree(0,0,N)
print("".join(map(str,(result))))
































### 실패한 코드 ###
# ## [입력]
# import sys
# input = sys.stdin.readline
# N = int(input())

# # String도 Iterable이라는 걸 기억하자.
# image = [ list(map(int, input().rstrip())) for _ in range(N) ]

# ## [입력 및 데이터 처리 테스트]
# # for i in range(N):
# #     for j in range(N):
# #         print(image[i][j], end=' ')
# #     print()

# def get_quadtree(image: list[list]):
#     print("(", end='')

#     half_row = len(image) // 2
#     top_left_row = image[:half_row]

#     ## top_left
#     top_left = []
#     for i in range(len(top_left_row)):
#         top_left.append(top_left_row[i][:half_row])

#     # half_row == len(top_left)
#     element_to_compare = top_left[0][0]
#     IS_SAME = True
#     for i in range(half_row):
#         for j in range(half_row):
#             if element_to_compare != top_left[i][j]:
#                 get_quadtree(top_left)
#                 IS_SAME = False
#         if not IS_SAME:
#             break
    
#     # print(f"SAME elem: {element_to_compare}, i: {i}, j: {j}, image: {top_left}")
#     # print("FINISHED: " + str(top_left))
#     print(element_to_compare, end='')

#     # top_right
#     # bottom_left
#     # bottom_right

#     print(")", end='')


# get_quadtree(image)
