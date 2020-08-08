mem = {}


def recDC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        mem[change] = 1
        return 1
    elif change in mem.keys():
        return mem[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change - i)
            if numCoins <= minCoins:
                minCoins = numCoins
                mem[change] = minCoins
    return minCoins


if __name__ == '__main__':
    print(recDC([1, 5, 10, 25], 63))
