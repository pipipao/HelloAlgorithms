def crot(x,y,n,m):
    return y,n-x+1,m,n
def rcroy(x,y,n,m):
    return m-y+1,x,m,n
def hrot(x,y,n,m):
    return x,m-y+1,n,m
clock,hrev,reclock=map(int,input().split())
nn,mm=map(int,input().split())
for _ in range(int(input())):
    x,y=map(int,input().split())
    n=nn
    m=mm
    for _ in range(clock):
        x,y,n,m=crot(x,y,n,m)
    for _ in range(hrev):
        x,y,n,m=hrot(x,y,n,m)
    for _ in range(reclock):
        x,y,n,m=rcroy(x,y,n,m)
    print(x,y)
