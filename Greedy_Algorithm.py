# 硬貨の問題
def coin():
	v = [1, 5, 10, 50, 100, 500]
	c = [3, 2, 1, 3, 0, 2]
	a = 620
	ans = 0

	for i in range(5, -1, -1):
		t = min(a // v[i], c[i])
		a -= t * v[i]
		ans += t

	print(ans)


# 区間スケジューリング問題
def schedule():
	n = 5
	s = [1, 2, 4, 6, 8]
	t = [3, 5, 7, 9, 10]
	itv = []
	for i in range(n):
		itv.append([t[i], s[i]])
	itv.sort()

	ans = 0
	t = 0
	for i in range(n):
		if t < itv[i][1]:
			ans += 1
			t = itv[i][0]
	print(ans)


# 辞書最小問題
def Best_Cow_Line():
	S = 'ACDBCB'
	N = len(S)

	a = 0
	b = N - 1

	while a <= b:
		left = False
		for i in range(b + 1):
			if S[a + i] < S[b - i]:
				left = True
				break
			elif S[a + i] > S[b - i]:
				left = False
				break
		if left:
			print(S[a], end='')
			a += 1
		else:
			print(S[b], end='')
			b -= 1
	print()


# Saruman's Army
def Saruman_Army():
	N = 6
	R = 10
	X = [1, 7, 15, 20, 30, 50]

	X.sort()

	i = 0
	ans = 0
	while i < N:
		s = X[i]
		i += 1

		while i < N and X[i] <= s + R:
			i += 1
		p = X[i - 1]

		while i < N and X[i] <= p + R:
			i += 1
		ans += 1

	print(ans)


# Fence Repair
def Fence_Repair():
	N = 3
	L = [8, 5, 8]

	ans = 0

	while N > 1:
		mil1 = 0
		mil2 = 1

		if L[mil1] > L[mil2]:
			mil1, mil2 = mil2, mil1

		for i in range(2, N):
			if L[i] < L[mil1]:
				mil2 = mil1
				mil1 = i
			elif L[i] < L[mil2]:
				mil2 = i

		t = L[mil1] + L[mil2]
		ans += t

		if mil1 == N:
			mil1, mil2 = mil1, mil2

		L[mil1] = t
		L[mil2] = L[N - 1]
		N -= 1

	print(ans)

if __name__ == '__main__':
	coin()
	schedule()
	Best_Cow_Line()
	Saruman_Army()
	Fence_Repair()













