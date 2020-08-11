def bubbleSort(l):
    for i in range(len(l) - 1, 0, -1):
        for j in range(i):
            if l[j] > l[j + 1]:
                t = l[j + 1]
                l[j + 1] = l[j]
                l[j] = t


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    bubbleSort(alist)
    print(alist)
