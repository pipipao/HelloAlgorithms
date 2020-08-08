def convBase(n, base):
    dig = "0123456789ABCDEF"
    if n < base:
        return dig[n]
    return convBase(n // base, base) + dig[n % base]


if __name__ == '__main__':
    print(convBase(255, 16))
