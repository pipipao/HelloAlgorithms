n, times = map(int, input().split())
sl = list(map(int, input().split()))
cmd_l = []
for _ in range(times):
    cmd_l.append(input())


def query(l, r):
    if l > r:
        print(max(sl[r - 1:l]))
    else:
        print(max(sl[l - 1:r]))


def upgrade(sid, score):
    sl[sid - 1] = score


for cmd in cmd_l:
    cs = cmd.split()
    letter = cs[0]
    a = int(cs[1])
    b = int(cs[2])
    if letter == 'Q':
        query(a, b)
    else:
        upgrade(a, b)
