N = int(input())
mat = []
for _ in range(N):
    rowin = list(map(int, input().split()))
    mat.append(rowin)

while len(mat) > 0:
    maxrsum=0
    maxcsum=0
    maxr = 0
    maxc = 0
    for row in range(len(mat)):
        rsum=sum(mat[row])
        if rsum>maxrsum:
            maxrsum=rsum
            maxr=row
    for col in range(len(mat)):
        csum=0
        for rr in mat:
            csum+=rr[col]
        if csum>maxcsum:
            maxc=col
            maxcsum=csum
    print((maxr + 1), (maxc + 1))
    mat.pop(maxr)
    for rr in mat:
        rr.pop(maxc)
