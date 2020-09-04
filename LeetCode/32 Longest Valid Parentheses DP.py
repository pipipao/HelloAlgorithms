class Solution:
    def longestValidParentheses(self, s: str) -> int:
        length=len(s)
        dp=[0 for _ in range(length+1)]
        for i in range(length-1,-1,-1):
            if s[i]=='(':
                if i<length-1:
                    if s[i+1]==')':
                        dp[i]=2
                        if i+2<length:
                            dp[i]=dp[i+2]+2
                    if s[i+1]=='(':
                        right=i+dp[i+1]+1
                        if right<length and s[right]==')':
                            dp[i]=right-i+1
                            if right+1<length:
                                dp[i]=dp[right+1]+dp[i]
        return max(dp)