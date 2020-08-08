n, times = map(int, input().split())
l = list(map(int, input().split()))
for _ in range(times):
    counter = 0
    target = int(input())
    for i in range(len(l)):
        if l[i] >= target:
            l[i] -= 1
            counter += 1
    print(counter)
