class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        x=len(word1)
        y=len(word2)
        dp=[[None]*(y+1) for _ in range(x+1)]
        for i in range(x+1):
            for j in range(y+1):
                if i==0:
                    dp[i][j]=j
                elif j==0:
                    dp[i][j]=i
                else:
                    if word1[i-1]==word2[j-1]:
                        dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]-1)
                    else:
                        dp[i][j]=1+min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])
        return dp[x][y]

# 巨坑
# [[None]*x]*y
# 这样生成的多维list是个大坑
# 每一行都指向的是同一个地址
# 修改任意一行其他的行也会跟着变