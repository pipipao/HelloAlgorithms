goodsList = list(map(int, input().split(',')))
room = int(input())
maxs = set()


def recM(left, gl, currentNum):
    if gl:
        for good in gl:
            if good <= left:
                leftGL=gl
                leftGL.remove(good)
                recM(left - good, leftGL, currentNum + 1)
    maxs.add(currentNum)

recM(room, goodsList, 0)
print(max(maxs))
