def subrec(n, cnum, c, fobs, curl,res):
    if curl==n:
        res[n]+=1
        res[n]%=(10^9+7)
        return
    elif curl<n:
        for i in range(cnum):
            if (i+1) not in fobs[c]:
                subrec(n,cnum,i,fobs,curl+1,res)

def rec(n,cnum,fobs):
    res={}
    res[n]=0
    for i in range(cnum):
        subrec(n,cnum,i,fobs,1,res)
    return res[n]
T=int(input())
for _ in range(T):
    n,cnum,knum=map(int,input().split())
    fobs=[]
    for _ in range(cnum):
        fob=list(map(int,input().split()))
        fobs.append(fob)
    print(rec(n,cnum,fobs))

