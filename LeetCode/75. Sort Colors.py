class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        zero,two=0,n-1
        i=0
        while i <= two:
            if nums[i]==0:
                nums[i]=nums[zero]
                nums[zero]=0
                zero+=1
            if nums[i]==2:
                nums[i]=nums[two]
                nums[two]=2
                two-=1
                if nums[i]!=1:
                    i-=1
            i+=1