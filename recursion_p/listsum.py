def listsum(s):
    if len(s) == 1:
        return s[0]
    else:
        return s[0] + listsum(s[1:])


if __name__ == '__main__':
    print(listsum([1, 2, 3, 4]))
