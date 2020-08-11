def selectionSort(l):
    for targetSlot in range(len(l) - 1, 0, -1):
        maxPos = 0
        for i in range(1, targetSlot + 1):
            if l[i] > l[maxPos]:
                maxPos = i
        t = l[targetSlot]
        l[targetSlot] = l[maxPos]
        l[maxPos] = t


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selectionSort(alist)
    print(alist)
