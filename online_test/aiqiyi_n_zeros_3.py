n = int(input())
cur=1
counter = 0
for i in range(1, n + 1):
    num = cur * (i + 1)
    while num % 10 == 0:
        num /= 10
        counter += 1
    cur = int(num)
print(counter)
