def solve():
    avilableAnswer=False
    isEnd=False
    res=[]
    def dfs(param, current):
        if avilableAnswer:
            res.append(current)
        if isEnd:
            return
        for x in param:
            dfs(param,current.append(x))

