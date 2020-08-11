times = int(input())
nl = []
for _ in range(times):
    nl.append(int(input()))
mem = {}


def recDC(n):
    if n == 3:
        return 3
    elif n == 2:
        return 2
    elif n == 1:
        return 1
    elif n < 1:
        return 0
    if n in mem.keys():
        return mem[n]
    return recDC(n - 1) + 2 + recDC(n - 2) + 3 + recDC(n - 3)


for n in nl:
    print(recDC(n))
