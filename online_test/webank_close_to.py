length,times=map(int,input().split())
l=list(map(int,input().split()))
l.sort()
qnum=[]
for _ in range(times):
    qnum.append(int(input()))
for num in qnum:
    if length<1:
        continue
    md=abs(num-l[0])
    res=l[0]
    flag=False
    for n in l:
        d=abs(n-num)
        if d<md:
            md=d
            res=n
            flag=True
        elif flag:
            break
    print(res)
