def insertionSort(l):
    for index in range(1, len(l)):
        value = l[index]
        position = index
        while position > 0 and l[position - 1] > value:
            l[position] = l[position - 1]
            position -= 1
        l[position] = value


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertionSort(alist)
    print(alist)
