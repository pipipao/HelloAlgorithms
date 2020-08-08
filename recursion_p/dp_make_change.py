def dpMakechange(coinValueList, change):
    mem = [change]*(change+1)
    for cents in range(change + 1):
        num = cents
        for j in [c for c in coinValueList if c <= change]:
            if mem[cents - j] + 1 < num:
                num = mem[cents - j] + 1
        mem[cents] = num
    return mem[change]

if __name__ == '__main__':
    print(dpMakechange([1,5,10,25],63))
