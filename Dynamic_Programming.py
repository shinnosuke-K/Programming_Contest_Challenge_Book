# ナップザック問題
def knapsack(i, j):
	n = 4
	w = [2, 1, 3, 2]
	v = [3, 2, 4, 2]

	res = 0
	if i == n:
		res = 0
	elif j < w[i]:
		res = knapsack(i + 1, j)
	else:
		res = max(knapsack(i + 1, j), knapsack(i + 1, j - w[i]) + v[i])

	return res


# ナップザック問題 改良
dp = [[-1 for i in range(6)] for j in range(5)]
def knapsack_ref(i, j):
	n = 4
	w = [2, 1, 3, 2]
	v = [3, 2, 4, 2]

	if dp[i][j] >= 0:
		return dp[i][j]

	res = 0
	if i == n:
		res = 0
	elif j < w[i]:
		res = knapsack_ref(i + 1, j)
	else:
		res = max(knapsack_ref(i + 1, j), knapsack_ref(i + 1, j - w[i]) + v[i])

	dp[i][j] = res
	return dp[i][j]


# ナップザック問題 再帰
def knapsack_rec():
	dp = [[0 for i in range(6)] for j in range(5)]
	n = 4
	w = [2, 1, 3, 2]
	v = [3, 2, 4, 2]
	W = 5

	for i in range(n - 1, -1, -1):
		for j in range(W + 1):
			if j < w[i]:
				dp[i][j] = dp[i + 1][j]
			else:
				dp[i][j] = max(dp[i + 1][j], dp[i + 1][j - w[i]] + v[i])

	print(dp[0][W])


# Longest Common Subsequence
def lcs():
	s = 'abcd'
	t = 'becd'
	n = len(s)
	m = len(t)
	dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

	for i in range(n):
		for j in range(m):
			if s[i] == t[j]:
				dp[i + 1][j + 1] = dp[i][j] + 1
			else:
				dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
	print(dp[n][m])


# 個数制限なしナップザック問題
def knapsack_no_qua():
	n = 3
	w = [3, 4, 2]
	v = [4, 5, 3]
	W = 7
	dp = [[0 for i in range(W + 1)] for j in range(n + 1)]

	for i in range(n):
		for j in range(W + 1):
			for k in range(j + 1):
				if k * w[i] <= j:
					dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - k * w[i]] + k * v[i])

	print(dp[n][W])


# 個数制限なしナップザック問題 改良
def knapsack_no_qua_ref():
	n = 3
	w = [3, 4, 2]
	v = [4, 5, 3]
	W = 7
	dp = [[0 for i in range(W + 1)] for j in range(n + 1)]

	for i in range(n):
		for j in range(W + 1):
			if j < w[i]:
				dp[i + 1][j] = dp[i][j]
			else:
				dp[i + 1][j] = max(dp[i][j], dp[i + 1][j - w[i]] + v[i])

	print(dp[n][W])


# ナップザック問題 サイズ大きい
def knapsack_2():
	INF = 100000000
	n = 4
	w = [2, 1, 3, 2]
	v = [3, 2, 4, 2]
	W = 5
	dp = [[INF for i in range(n * len(v) + 1)] for j in range(n + 1)]
	dp[0][0] = 0

	for i in range(n):
		for j in range(n * len(v) + 1):
			if j < v[i]:
				dp[i + 1][j] = dp[i][j]
			else:
				dp[i + 1][j] = min(dp[i][j], dp[i][j - v[i]] + w[i])

	for i in range(n * len(v) + 1):
		if dp[n][i] <= W:
			res = i

	print(res)


if __name__ == '__main__':
	print(knapsack(0, 5))
	print(knapsack_ref(0, 5))
	knapsack_rec()
	lcs()
	knapsack_no_qua()
	knapsack_no_qua_ref()
	knapsack_2()


































