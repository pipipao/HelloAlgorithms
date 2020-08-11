class Node():
    def __init__(self, x):
        self.val = x
        self.next = None


n, rt = map(int, input().split())
l = []
for i in range(1, n + 1):
    l.append(Node(i))
for _ in range(rt):
    pre, nxt = map(int, input().split())
    l[pre - 1].next = l[nxt]
res = 0
check = set()
for nod in l:
    if nod in check:
        continue
    for k in range(n):
        check.add(nod)
        if nod.next is None:
            break
        nod = nod.next
        if nod in check:
            res += (k * (k - 1) / 2)
print(res)
