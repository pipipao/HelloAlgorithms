def moveDisk(height, fromPole, withPole, toPole):
    if height >= 1:
        moveDisk(height - 1, fromPole, toPole, withPole)
        move(fromPole, toPole)
        moveDisk(height - 1, withPole, toPole, fromPole)


def move(f, t):
    print('Moving disk form ' + f + ' to ' + t)


if __name__ == '__main__':
    moveDisk(5, 'A', 'B', 'C')
