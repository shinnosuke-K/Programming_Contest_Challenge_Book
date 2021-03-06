# ヒープの実装例
class Queue:
    heap = []
    sz = 0

    def push(self, x):
        i = self.sz
        self.sz += 1

        while i > 0:
            p = (i - 1) / 2

            if self.heap[p] <= x:
                break

            self.heap[i] = self.heap[p]
            i = p

        self.heap[i] = x

    def pop(self):
        ret = self.heap[0]
        self.sz -= 1
        x = self.heap[self.sz]

        i = 0
        while i * 2 + 1 < self.sz:
            a = i * 2 + 1
            b = i * 2 + 2

            if b < self.sz and self.heap[b] < self.heap[a]:
                a = b

            if self.heap[a] >= x:
                break

            self.heap[i] = self.heap[a]
            i = a

        self.heap[i] = x
        return ret


# Expedition import heapq
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


# 二分木の実装(たぶん)
class Node():
    def __init__(self, x):
        self.val = x
        self.lch = None
        self.rch = None


def insert(p, x):
    if p is None:
        q = Node(x)
        return q
    else:
        if x < p.val:
            p.lch = insert(p.lch, x)
            p.rch = insert(p.rch, x)
            return p


def binary_find(p, x):
    if p is None:
        return False
    elif x == p.val:
        return True
    elif x < p.val:
        return binary_find(p.lch, x)
    else:
        return binary_find(p.rch, x)


def remove(p, x):
    if p is None:
        return None
    elif x < p.val:
        p.lch = remove(p.lch, x)
    elif x > p.val:
        p.rch = remove(p.rch, x)
    elif p.lch is None:
        q = p.lch
        q.rch = p.rch
        del p
        return q
    else:
        q = Node()
        q = p.lch
        while q.rch.rch is not None:
            q = q.rch

        r = q.rch
        p.rch, r.lch, r.rch = r.lch, p.lch, p.rch
        del p
        return q


# Union-Findの実装
par = []
rank = []
def init(n):
    for i in range(n):
        par.append(i)
        rank.append(0)


def union_find(x):
    if par[x] == x:
        return x
    else:
        par[x] = union_find(par[x])
        return par[x]


def unite(x, y):
    x = union_find(x)
    y = union_find(y)

    if x == y:
        return

    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1


def same(x, y):
    return union_find(x) == union_find(y)


# 食物連鎖
def Food_chain():
    N = 100
    K = 7

    T = [1, 2, 2, 2, 2, 1, 2, 1]
    X = [101, 1, 2, 3, 1, 3, 5]
    Y = [1, 2, 3, 3, 3, 1, 5]

    init(N * 3)

    ans = 0

    for i in range(K):
        t = T[i]
        x = X[i] - 1
        y = Y[i] - 1

        if x < 0 or N <= x or y < 0 or N <= y:
            ans += 1
            continue

        if t == 1:
            if same(x, y + N) or same(x, y + 2 * N):
                ans += 1
            else:
                unite(x, y)
                unite(x + N, y + N)
                unite(x + N * 2, y + N * 2)
        else:
            if same(x, y) or same(x, y + 2 * N):
                ans += 1
            else:
                unite(x, y + N)
                unite(x + N, y + 2 * N)
                unite(x + 2 * N, y)

    print(ans)


if __name__ == '__main__':
    Expedition()
    Fence_Repair()
    root = Node(1)
    root = insert(root, 1)
    binary_find(root, 1)
    # init(10)
    # print(union_find(3))
    # unite(1, 8)
    # print(same(3, 8))
    Food_chain()
