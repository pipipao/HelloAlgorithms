times = int(input())
cmds = []
for _ in range(times):
    cmds.append(input())
for cmd in cmds:
    w = set()
    b = set()
    t = set()
    pais = list(cmd.split())
    for pai in pais:
        num = int(pai[0])
        huase = pai[1]
        if huase == 'W':
            w.add(num)
        elif huase == 'B':
            b.add(num)
        else:
            t.add(num)
    if len(w) + len(b) + len(t) != 7:
        print('NO')
    else:
        checka = {1, 4, 7}
        checkb = {2, 5, 8}
        checkc = {3, 6, 9}
        wf = bf = tf = False
        if w <= checka or w <= checkb or w <= checkc:
            wf = True
        if b <= checka or b <= checkb or b <= checkc:
            bf = True
        if t <= checka or t <= checkb or t <= checkc:
            tf = True
        if wf and bf and tf:
            print('YES')
        else:
            print('NO')
