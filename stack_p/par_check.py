from stack_p.stack_practice import Stack


def parChecker(str):
    s = Stack()
    for c in str:
        if c in '([{':
            s.push(c)
        elif s.isEmpty():
            return False
        elif c in ')]}':
            if not matches(s.pop(), c):
                return False

    if s.isEmpty():
        return True
    return False


def matches(open, close):
    opens = '([{'
    closes = ')]}'
    return opens.index(open) == closes.index(close)


if __name__ == '__main__':
    print(parChecker('()()()()()('))
    print(parChecker(')(())'))
    print(parChecker('(((x))(y))'))
    print(parChecker('{[()]}'))
    print(parChecker('{[(([)]}'))
