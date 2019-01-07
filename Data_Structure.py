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

