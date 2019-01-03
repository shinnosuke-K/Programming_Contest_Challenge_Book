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


# 個数制限付き部分和問題
def Partial_Sum_Problem():
	n = 3
	a = [3, 5, 8]
	m = [3, 2, 2]
	K = 18
	dp = [[False for i in range(K + 1)] for j in range(n + 1)]

	dp[0][0] = True

	for i in range(n):
		for j in range(K + 1):
			for k in range(j + 1):
				if k <= m[i] and k * a[i] <= j:
					break
				else:
					dp[i + 1][j] |= dp[i][j - k * a[i]]

	if dp[n][K]:
		print('Yes')
	else:
		print('No')


# 個数制限付き部分和問題 配列再利用
def Partial_Sum_Problem_reuse():
	n = 3
	a = [3, 5, 8]
	m = [3, 2, 2]
	K = 18
	dp = [-1 for i in range(K + 1)]
	dp[0] = 0

	for i in range(n):
		for j in range(K + 1):
			if dp[j] >= 0:
				dp[j] = m[i]
			elif j < a[i] or dp[j - a[i]] <= 0:
				dp[j] = -1
			else:
				dp[j] = dp[j - a[i]] - 1

	if dp[K] >= 0:
		print('Yes')
	else:
		print('No')


# Longest Increasing Subsequence
def lis():
	n = 5
	a = [4, 2, 3, 1, 5]
	dp = [0 for i in range(n)]

	res = 0
	for i in range(n):
		dp[i] = 1
		for j in range(i):
			if a[j] < a[i]:
				dp[i] = max(dp[i], dp[j] + 1)
		res = max(res, dp[i])
	print(res)


# 分割数
def Division_Number():
	n = 4
	m = 3
	M = 10000
	dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
	dp[0][0] = 1

	for i in range(1, m + 1):
		for j in range(n + 1):
			if j - i >= 0:
				dp[i][j] = (dp[i - 1][j] + dp[i][j - i]) % M
			else:
				dp[i][j] = dp[i - 1][j]

	print(dp[m][n])


# 重複組み合わせ問題
def Overlapping_Combination():
	n = 3
	m = 3
	a = [1, 2, 3]
	M = 10000
	dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

	for i in range(n + 1):
		dp[i][0] = 1

	for i in range(n):
		for j in range(1, m + 1):
			if j - 1 - a[i] >= 0:
				dp[i + 1][j] = (dp[i + 1][j - 1] + dp[i][j] - dp[i][j - 1 - a[i]] + M) % M
			else:
				dp[i + 1][j] = (dp[i + 1][j - 1] + dp[i][j]) % M

	print(dp[n][m])


if __name__ == '__main__':
	print(knapsack(0, 5))
	print(knapsack_ref(0, 5))
	knapsack_rec()
	lcs()
	knapsack_no_qua()
	knapsack_no_qua_ref()
	knapsack_2()
	Partial_Sum_Problem_reuse()
	Partial_Sum_Problem_reuse()
	lis()
	Division_Number()
	Overlapping_Combination()
