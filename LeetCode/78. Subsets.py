from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=list()

        # 具体的递归函数
        def dfs(current,index):
            # 满足要求或者递归终止
            if index>=len(nums):
                res.append(current)
                return
            dfs(current,index+1)
            dfs(current+[nums[index]],index+1)
        dfs([],0)
        return res
