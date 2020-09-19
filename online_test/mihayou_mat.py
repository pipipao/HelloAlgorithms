al='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
table=[]
for c in al:
    table.append(c)
m,n=map(int,input().split())
res=[[None]*n for _ in range(m)]
check=set()
right=down=left=up=False
x=y=0
counter=1
right=True
res[0][0]='A'
check.add((0,0))
while len(check)<(m*n):
    if right:
        if y + 1 >= n or (x, y + 1) in check:
            right = False
            down = True
        else:
            y += 1
            res[x][y]=table[counter]
            counter+=1
            counter%=26
            check.add((x, y))
    if down:
        if x + 1 >= m or (x + 1, y) in check:
            down = False
            left = True
        else:
            x += 1
            res[x][y] = table[counter]
            counter += 1
            counter %= 26
            check.add((x, y))
    if left:
        if y - 1 < 0 or (x, y - 1) in check:
            left = False
            up = True
        else:
            y -= 1
            res[x][y] = table[counter]
            counter += 1
            counter %= 26
            check.add((x, y))
    if up:
        if x - 1 < 0 or (x - 1, y) in check:
            up = False
            right = True
        else:
            x -= 1
            res[x][y] = table[counter]
            counter += 1
            counter %= 26
            check.add((x, y))
if m==0 or n==0:
    print(None)
else:
    for row in res:
        print(' '.join(row))

