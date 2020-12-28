class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre=0
        maxTotal=nums[0]
        for n in nums:
            pre=max(pre+n,n)
            maxTotal=max(pre,maxTotal)
        return maxTotal