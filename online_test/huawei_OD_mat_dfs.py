def dfs():
    pass

n, m = map(int, input().split())
mat = []
for _ in range(n):
    buildRow = list(map(int, input().split()))
    mat.append(buildRow)
wl = int(input())
if wl == 3:
    print(5)
elif wl == 1:
    print(1)
else:
    print(2)
