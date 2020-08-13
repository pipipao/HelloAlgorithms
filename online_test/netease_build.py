for _ in range(int(input())):
    cmdn = int(input())
    cmds = []
    for _ in range(cmdn):
        cmds.append(input())
    time_list = []
    id_list = []
    status_list = []
    for cmd in cmds:
        time, id, status = map(int, cmd.split())
        time_list.append(time)
        id_list.append(id)
        status_list.append(status)
    id_stack=[]
    time_stack=[]
    d=dict()
    for id in id_list:
        d[id]=0
    maxtime=0
    qiant=0
    for i in range(cmdn):
        if status_list[i]==0:
            if len(id_stack)>0:
                d[id_stack[-1]]+=time_list
            id_stack.append(id_list[i])
        else:
            id_stack.pop()



