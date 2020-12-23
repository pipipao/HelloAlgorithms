class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def dfs(nums,left,index,comb):
            if left==0:
                res.append(comb)
                return
            if index>=len(nums):
                return
            dfs(nums,left,index+1,comb)
            if left>=nums[index]:
                dfs(nums,left-nums[index],index,comb+[nums[index]])
        dfs(candidates,target,0,[])
        return res