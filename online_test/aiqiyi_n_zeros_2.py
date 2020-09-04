n = int(input())

mem = [0] * (n + 2)
mem[1] = 1
counter = 0
for i in range(1, n + 1):
    if mem[i]>1000000:
        mys=str(mem[i])
        mys=mys[::-1]
        mys=mys[:6]
        mys=mys[::-1]
        mem[i]=int(mys)
    num = mem[i] * (i + 1)
    while num % 10 == 0:
        num /= 10
        counter += 1
    mem[i + 1] = int(num)
print(mem[n])
print(counter)
# 8222838654177922817725562880000000

