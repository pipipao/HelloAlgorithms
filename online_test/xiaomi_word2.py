word = input()
mymap = [

    ['A', 'B', 'C', 'E'],

    ['S', 'F', 'C', 'S'],

    ['A', 'D', 'E', 'E']

]
def search(x,y,curi,word,flag,check:set):
    check.add((x,y))
    if curi==len(word)-1 and mymap[x][y]==word[curi]:
        flag=True
        print(True)
        return True
    if x==0:
        if y==0:
            if (x+1,y) not in check:
                search(x+1,y,curi+1,word,flag,check)
            if (x,y+1) not in check:
                search(x,y+1,curi,word,flag,check)
        elif y==3:
            if (x+1,y) not in check:
                search(x + 1, y, curi + 1, word, flag, check)
            if (x,y-1) not in check:
                search(x, y-1, curi + 1, word, flag, check)
        else:
            if (x+1,y) not in check:
                search(x + 1, y, curi + 1, word, flag, check)
            if (x,y-1) not in check:
                search(x, y-1, curi + 1, word, flag, check)
            if (x,y+1) not in check:
                search(x,y+1,curi,word,flag,check)
    elif x==2:
        if y==0:
            if (x-1,y) not in check:
                search(x-1,y,curi+1,word,flag,check)
            if (x,y+1) not in check:
                search(x,y+1,curi,word,flag,check)
        elif y==3:
            if (x-1,y) not in check:
                search(x - 1, y, curi + 1, word, flag, check)
            if (x,y-1) not in check:
                search(x, y-1, curi + 1, word, flag, check)
        else:
            if (x-1,y) not in check:
                search(x - 1, y, curi + 1, word, flag, check)
            if (x,y-1) not in check:
                search(x, y-1, curi + 1, word, flag, check)
            if (x,y+1) not in check:
                search(x,y+1,curi,word,flag,check)
    elif y==0:
        if (x - 1, y) not in check:
            search(x - 1, y, curi + 1, word, flag, check)
        if (x, y + 1) not in check:
            search(x, y + 1, curi, word, flag, check)
        if (x + 1, y) not in check:
            search(x + 1, y, curi + 1, word, flag, check)
    elif y==3:
        if (x - 1, y) not in check:
            search(x - 1, y, curi + 1, word, flag, check)
        if (x, y - 1) not in check:
            search(x, y - 1, curi + 1, word, flag, check)
        if (x + 1, y) not in check:
            search(x + 1, y, curi + 1, word, flag, check)
    else:
        if (x - 1, y) not in check:
            search(x - 1, y, curi + 1, word, flag, check)
        if (x, y - 1) not in check:
            search(x, y - 1, curi + 1, word, flag, check)
        if (x + 1, y) not in check:
            search(x + 1, y, curi + 1, word, flag, check)
        if (x, y + 1) not in check:
            search(x, y + 1, curi, word, flag, check)




length=len(word)
startw=word[0]
sset=set()
for i in range(3):
    for j in range(4):
        if mymap[i][j]==startw:
            sset.add((i,j))
flag=False
for start in sset:
    x=start[0]
    y=start[1]
    search(x,y,0,word,flag,set())
# if flag:
#     print('true')
# else:
#     print('false')
