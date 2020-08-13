N=int(input())
mat=[]
for _ in range(N):
    rowin=list(map(int,input().split()))
    mat.append(rowin)


while len(mat)>0:
    maxsum=0
    maxr=0
    maxc=0
    for row in range(len(mat)):
        for col in range(len(mat)):
            suma=sum(mat[row])
            sumb=0
            for rr in mat:
                sumb+=rr[col]
            mysum=suma+sumb-mat[row][col]
            if mysum>maxsum:
                maxsum=mysum
                maxr=row
                maxc=col
    print((maxr+1),(maxc+1))
    mat.pop(maxr)
    for rr in mat:
        rr.pop(maxc)