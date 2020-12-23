class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False) - 1
        if left <= right < len(nums) and nums[left] == target and nums[right] == target:
            return [left, right]
        return [-1, -1]

    def binarySearch(self, nums, target, isFindingLeft):
        left = 0
        right = len(nums) - 1
        ans = len(nums)
        while left <= right:
            mid = int((left + right) / 2)
            if (nums[mid] > target) or (isFindingLeft and nums[mid] >= target):
                right = mid - 1
                ans = mid
            else:
                # Find the first num that bigger than target
                left = mid + 1
        return ans
