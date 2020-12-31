class Solution:
    def climbStairs(self, n: int) -> int:
        i=j=1
        for k in range(n):
            temp=i
            i=j
            j=temp+j
        return i