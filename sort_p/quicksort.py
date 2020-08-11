def partition(ls, first, last):
    pv = ls[first]
    l = first + 1
    r = last
    done = False
    while not done:
        while l <= r and ls[l] <= pv:
            l += 1
        while l <= r and ls[r] >= pv:
            r -= 1
        if l > r:
            done = True
        else:
            t = ls[r]
            ls[r] = ls[l]
            ls[l] = t
    t = ls[r]
    ls[r] = ls[first]
    ls[first] = t
    return r


def recQS(l, first, last):
    if first < last:
        sp = partition(l, first, last)
        recQS(l, first, sp - 1)
        recQS(l, sp + 1, last)


def quickSort(l):
    recQS(l, 0, len(l) - 1)


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quickSort(alist)
    print(alist)
