# 암호 만들기

length = int(input().split()[0])
alphas = sorted(input().split())

def backtrack(depth, idx, num_v, num_c, current_str:list):
    if depth == length:
        print(''.join(current_str))
        return

    for i in range(idx, len(alphas)):
        is_v = alphas[i] in 'aeiou'
        if is_v and length - depth <= 2 - num_c:
            continue
        if not is_v and length - depth <= 1 - num_v:
            continue
        current_str.append(alphas[i])
        backtrack(depth + 1, i + 1, num_v + is_v, num_c + (not is_v), current_str)
        current_str.pop()

backtrack(0, 0, 0, 0, [])