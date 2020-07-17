def birthday():
    p = 1
    for i in range(365, 355, -1):
        p = p * (i / 365)
    print(1 - p)


if __name__ == '__main__':
    birthday()
