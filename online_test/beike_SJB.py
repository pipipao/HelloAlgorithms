def win(a, b, c):
    suma = 0
    if a == 'S':
        if b == 'S':
            suma -= 1
        if b == 'J':
            suma += 1
        if b == 'B':
            suma -= 1
        if c == 'S':
            suma -= 1
        if c == 'J':
            suma += 1
        if c == 'B':
            suma -= 1
    if a == 'J':
        if b == 'J':
            suma -= 1
        if b == 'S':
            suma -= 1
        if b == 'B':
            suma += 1
        if c == 'J':
            suma -= 1
        if c == 'S':
            suma -= 1
        if c == 'B':
            suma += 1
    if a == 'B':
        if b == 'B':
            suma -= 1
        if b == 'S':
            suma += 1
        if b == 'J':
            suma -= 1
        if c == 'B':
            suma -= 1
        if c == 'S':
            suma += 1
        if c == 'J':
            suma -= 1
    return suma


T = int(input())
rounds = []
for _ in range(T):
    round = list(input().split())
    rounds.append(round)
for round in rounds:
    left = round[0]
    right = round[1]
    b = round[2]
    c = round[3]
    ln = win(left, b, c)
    rn = win(right, b, c)
    if ln == rn:
        print('same')
    elif ln > rn:
        print('left')
    else:
        print('right')
