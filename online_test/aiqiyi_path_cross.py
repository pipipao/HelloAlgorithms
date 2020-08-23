cmds = input()
site = set()
x = 0
y = 0
flag=False
for cmd in cmds:
    site.add((x, y))
    if cmd == 'E':
        x += 1
    if cmd == 'W':
        x -= 1
    if cmd == 'N':
        y += 1
    if cmd == 'S':
        y -= 1
    if (x,y) in site:
        flag=True
        break
print(flag)
