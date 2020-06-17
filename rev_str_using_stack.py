from stack_practice import Stack


def revstring(mystr):
    s = Stack()
    for c in mystr:
        s.push(c)
    ans = ""
    for i in range(s.size()):
        ans += s.pop()
    return ans


def testEqual(str1, str2):
    if str1 == str2:
        print('Pass')
    else:
        print('Error')


if __name__ == '__main__':
    testEqual(revstring('apple'), 'elppa')
    testEqual(revstring('x'), 'x')
    testEqual(revstring('1234567890'), '0987654321')
