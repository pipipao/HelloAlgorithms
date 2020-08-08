from queue_p.deque import Deque


def palchecker(s):
    dq = Deque()
    for c in s:
        dq.addRear(c)
    flag = True
    while dq.size() > 1:
        l = dq.removeRear()
        r = dq.removeFront()
        if l != r:
            flag = False
            break
    return flag


if __name__ == '__main__':
    print(palchecker('adccda'))

