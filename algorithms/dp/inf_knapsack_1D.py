def pack(w, v, c):
    dp = [0 for _ in range(c + 1)]
    for i in range(len(w)):
        for j in range(c + 1):
            if j >= w[i]:
                dp[j] = max(dp[j], dp[j - w[i]] + v[i])
    return dp[-1]


if __name__ == '__main__':
    weight = [2, 2, 6, 5, 4]
    value = [3, 6, 5, 4, 6]
    c = 10
    print(pack(weight, value, c))
