# 迷路の最短路

INF = 100000000

maze = [
	['#', 'S', '#', '#', '#', '#', '#', '#', '.', '#'],
	['.', '.', '.', '.', '.', '.', '#', '.', '.', '#'],
	['.', '#', '.', '#', '#', '.', '#', '#', '.', '#'],
	['.', '#', '.', '.', '.', '.', '.', '.', '.', '.'],
	['#', '#', '.', '#', '#', '.', '#', '#', '#', '#'],
	['.', '.', '.', '.', '#', '.', '.', '.', '.', '#'],
	['.', '#', '#', '#', '#', '#', '#', '#', '.', '#'],
	['.', '.', '.', '.', '#', '.', '.', '.', '.', '.'],
	['.', '#', '#', '#', '#', '.', '#', '#', '#', '.'],
	['.', '.', '.', '.', '#', '.', '.', '.', 'G', '#']
]

N = 10
M = 10

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

sx = 0
sy = 1

gx = 9
gy = 8


def bfs_maze():
	d = [[INF for i in range(M)] for j in range(N)]
	que = []
	que.append([sx, sy])
	d[sx][sy] = 0

	while len(que):
		p_first  = que[0][0]
		p_second = que[0][1]

		que.pop(0)

		if p_first == gx and p_second == gy:
			break

		for i in range(4):
			nx = p_first  + dx[i]
			ny = p_second + dy[i]

			if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] != '#' and d[nx][ny] == INF:
				que.append([nx, ny])
				d[nx][ny] = d[p_first][p_second] + 1

	print(d[gx][gy])


if __name__ == '__main__':
	bfs_maze()
