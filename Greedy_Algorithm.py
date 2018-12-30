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

if __name__ == '__main__':
	coin()
	schedule()