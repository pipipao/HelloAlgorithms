from stack_p.stack_practice import Stack


def baseConverter(decNum, base):
    digits = "0123456789ABCDEF"
    s = Stack()
    while decNum > 0:
        rem = decNum % base
        s.push(rem)
        decNum //= base
    ans = ''
    while not s.isEmpty():
        ans += digits[s.pop()]
    return ans


if __name__ == '__main__':
    print(baseConverter(15, 16))
    print(baseConverter(15278, 16))
    print(baseConverter(1024, 2))
