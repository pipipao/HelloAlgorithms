class Solution:
    def canJump(self, nums: List[int]) -> bool:
        far=0
        for i in range(len(nums)):
            if far<i:
                return False
            far=max(i+nums[i],far)
        return True