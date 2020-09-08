l=input()
myl=[]
for c in l:
    if c in {'0','1','2','3','4','5','6','7','8','9'}:
        myl.append(int(c))
length=len(myl)
far=0
cur=0
while cur<length and cur<=far:
    far=max(cur+myl[cur],far)
    cur+=1
if cur==length:
    print('true')
else:
    print('false')