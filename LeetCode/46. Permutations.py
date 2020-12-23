class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(current,leftNums):
            if len(leftNums)==0:
                res.append(current)
            for i in range(len(leftNums)):
                dfs(current+[leftNums[i]],leftNums[:i]+leftNums[i+1:])
        dfs([],nums)
        return res