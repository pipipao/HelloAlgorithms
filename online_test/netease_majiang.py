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
        checka = [1, 4, 7]
        checkb = [2, 5, 8]
        checkc = [3, 6, 9]
        flag = False
        for ww in w:
            if ww in checka:
                flag = True
            if flag and ww not in checka:
                print('NO')
                continue

        for ww in w:
            if ww in checkb:
                flag = True
            if flag and ww not in checkb:
                print('NO')
                continue

        for ww in w:
            if ww in checkc:
                flag = True
            if flag and ww not in checkc:
                print('NO')
                continue

        flag = False
        for ww in b:
            if ww in checka:
                flag = True
            if flag and ww not in checka:
                print('NO')
                continue

        for ww in b:
            if ww in checkb:
                flag = True
            if flag and ww not in checkb:
                print('NO')
                continue

        for ww in b:
            if ww in checkc:
                flag = True
            if flag and ww not in checkc:
                print('NO')
                continue

        flag = False
        for ww in t:
            if ww in checka:
                flag = True
            if flag and ww not in checka:
                print('NO')
                continue

        for ww in t:
            if ww in checkb:
                flag = True
            if flag and ww not in checkb:
                print('NO')
                continue

        for ww in t:
            if ww in checkc:
                flag = True
            if flag and ww not in checkc:
                print('NO')
                continue

        print('YES')
