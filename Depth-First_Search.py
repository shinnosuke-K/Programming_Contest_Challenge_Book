
'''
問題:
整数a1、a2、...、an が与えられます。
その中からいくつか選び、
その和をちょうどkにすることができるかを判定しなさい。
制約:
1≦n≦20
-108≦ai≦108
-108≦ k ≦108

入力:
n = 4
a = {1, 2, 4, 7}
k = 13
'''


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


if __name__ == '__main__':
	if dfs(0, 0):
		print('Yes')
	else:
		print('No')
