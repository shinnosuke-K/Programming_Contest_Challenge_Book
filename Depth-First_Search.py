# 部分和問題
a = [1, 2, 4, 7]
n = len(a)
k = 18


def dfs(i, s):
    if i == n:
        return s == k
    if dfs(i + 1, s):
        return True
    if dfs(i + 1, s + a[i]):
        return True
    return False


# Lake Counting
N = 10
M = 12

field = [
    ['W', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', '.'],
    ['.', 'W', 'W', 'W', '.', '.', '.', '.', '.', 'W', 'W', 'W'],
    ['.', '.', '.', '.', 'W', 'W', '.', '.', '.', 'W', 'W', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', 'W', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.', 'W', '.', '.'],
    ['.', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.', '.'],
    ['.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', 'W', '.'],
    ['W', '.', 'W', '.', 'W', '.', '.', '.', '.', '.', 'W', '.'],
    ['.', 'W', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', '.'],
    ['.', '.', 'W', '.', '.', '.', '.', '.', '.', '.', 'W', '.']
]


def dfs_lc(x, y):
    field[x][y] = '.'

    for dx in range(-1, 2, 1):
        for dy in range(-1, 2, 1):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and field[nx][ny] == 'W':
                dfs_lc(nx, ny)
    return


def solve_lc():
    res = 0
    for i in range(0, N):
        for j in range(0, M):
            if field[i][j] == 'W':
                dfs_lc(i, j)
                res += 1
    print(res)


if __name__ == '__main__':

    # 部分和問題
    if dfs(0, 0):
        print('Yes')
    else:
        print('No')

    # Lake Counting
    solve_lc()
