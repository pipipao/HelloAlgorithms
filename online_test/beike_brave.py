n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
sl=len(a)//2
sr=sl+1

minh=0
def kill(l, r, hp,minhp):
    if l<=-1 and r>=len(a):
        if hp<=minhp:
            minh=hp
    if l<0:
        if hp>a[r]:
            hp=(hp-a[r]+b[r])
        else:
            d=a[r]-hp
            hp+=d
            hp = (hp - a[r] + b[r])
        kill(l,r+1,hp,minhp)
    elif r>=len(a):
        if hp>a[l]:
            hp=(hp-a[l]+b[l])
        else:
            d=a[r]-hp
            hp+=d
            hp = (hp - a[l] + b[l])
        kill(l-1,r,hp,minhp)
    else:
        if hp > a[r]:
            lhp = (hp - a[r] + b[r])
        else:
            lhp=hp
            d = a[r] - hp
            hp += d
            hp = (hp - a[r] + b[r])
        kill(l, r + 1, hp, minhp)