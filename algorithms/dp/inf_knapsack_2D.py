def pack(w, v, c):
    dp = [[0 for _ in range(c + 1)] for _ in range(len(w) + 1)]
    for i in range(1, len(w) + 1):
        for j in range(1, c + 1):
            if w[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - w[i - 1]] + v[i - 1])
    for row in dp:
        print(row)
    return dp[-1][-1]


if __name__ == '__main__':
    weight = [2, 2, 6, 5, 4]
    value = [3, 6, 5, 4, 6]
    c = 10
    print(pack(weight, value, c))
