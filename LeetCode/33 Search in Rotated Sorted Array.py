class Solution:
    def search(self, nums, target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            if nums[l]<nums[mid]:
                if nums[l]<=target and target<nums[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if nums[mid]<target and target<=nums[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1

if __name__ == '__main__':
    s=Solution()
    s.search([3,1],1)