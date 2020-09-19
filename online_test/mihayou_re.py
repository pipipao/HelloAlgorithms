targert=input()
res=input()

tarleng=len(targert)
resleng=len(res)
i=j=0
while i<tarleng and j<resleng:
    if targert[i]==res[j]:
        i+=1
        j+=1
    else:
        if res[j]=='.':
            i+=1
            j+=1
        elif res[j]=='+':
            res[j]=res[j-1]
        elif res[j]=='*':
            j-=1
if i==tarleng-1 and j==resleng-1:
    print('true')
else:
    print('false')

