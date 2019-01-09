# ヒープの実装例
class Queue:
	heap = []
	sz = 0

	def push(x):
		i = sz
		sz += 1

		while i > 0:
			p = (i - 1) / 2

			if heap[p] <= x:
				break

			heap[i] = heap[p]
			i = p

		heap[i] = x

	def pop():
		ret = heap[0]
		sz -= 1
		x = heap[sz]

		i = 0
		while i * 2 + 1 < sz:
			a = i * 2 + 1
			b = i * 2 + 2

			if b < sz and heap[b] < heap[a]:
				a = b

			if heap[a] >= x:
				break

			heap[i] = heap[a]
			i = a

		heap[i] = x
		return ret

# Expedition
import heapq
def Expedition():
	N = 4
	L = 25
	P = 10
	A = [10, 14, 20, 21]
	B = [10, 5, 2, 4]

	A.append(L)
	B.append(N)
	N += 1

	que = []

	ans = 0
	pos = 0
	tank = P

	for i in range(N):

		d = A[i] - pos

		while tank - d < 0:
			if len(que) == 0:
				# print(-1)
				return

			tank += heapq.heappop(que) * (-1)
			ans += 1

		tank -= d
		pos = A[i]
		heapq.heappush(que, B[i] * (-1))

	print(ans)

# Fence Repair
import heapq
def Fence_Repair():
	N = 3
	L = [8, 5, 8]

	ans = 0
	que = []

	for i in range(N):
		heapq.heappush(que, L[i])

	while len(que) > 1:
		l1 = heapq.heappop(que)
		l2 = heapq.heappop(que)

		ans += l1 + l2
		heapq.heappush(que, (l1 + l2))

	print(ans)


if __name__ == '__main__':
	Expedition()
	Fence_Repair()



















