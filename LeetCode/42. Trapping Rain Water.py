class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        lmax=0
        rmax=0
        ans=0
        while left<right:
            if height[left]<height[right]:
                if height[left]>=lmax:
                    lmax=height[left]
                else:
                    ans=ans+lmax-height[left]
                left=left+1
            else:
                if height[right]>=rmax:
                    rmax=height[right]
                else:
                    ans=ans+rmax-height[right]
                right=right-1
        return ans