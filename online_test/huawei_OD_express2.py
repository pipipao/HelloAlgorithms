goodsList = list(map(int, input().split(',')))
room = int(input())
maxs = dict()


def dpMaxNum(goodsList, room):
    mem = [0]*(room+1)
    for left in range(room + 1):
        num = 0
        for j in [c for c in goodsList if c <= left]:
            if mem[left - j] + 1 > num:
                num = mem[left - j] + 1
        mem[left] = num
    return mem[room]

print(dpMaxNum(goodsList,room))
