n = int(input())


def rec(n):
    if n == 1:
        return 1
    else:
        return n * rec(n - 1)


res = rec(n)
s = str(res)
s = s[::-1]
counter = 0
for c in s:
    if c == '0':
        counter += 1
    else:
        break
print(counter)
