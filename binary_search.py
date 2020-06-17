def binary_search(list, item):
    l = 0
    r = len(list) - 1
    while l <= r:
        mid = (l + r) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess < item:
            l = mid + 1
        if guess > item:
            r = mid - 1
    return None


# mid+1/-1 is necessary, or there may be a dead loop
if __name__ == '__main__':
    my_list = list(range(0, 30, 2))

    print(binary_search(my_list, 15))
    print(binary_search(my_list, -1))
    print(binary_search(my_list, 10))
