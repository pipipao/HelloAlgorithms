class Solution:
    def partition(self, nums, start, right):
        piv = nums[start]
        left = start
        left += 1
        done = False
        while not done:
            while left <= right and nums[left] <= piv:
                left += 1
            while left <= right and nums[right] >= piv:
                right -= 1
            if left > right:
                done = True
            else:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp
        t = nums[right]
        nums[right] = piv
        nums[start] = t
        return right

    def quickSelect(self, nums, left, right, target):
        if left==right:
            return nums[left]
        if left < right:
            cur = self.partition(nums, left, right)
            if cur == target:
                return nums[cur]
            if cur > target:
                return self.quickSelect(nums, left, cur - 1, target)
            else:
                return self.quickSelect(nums, cur + 1, right, target)

    def findKthLargest(self, nums, k: int) -> int:
        targert = len(nums) - k
        l = 0
        r = len(nums) - 1
        return self.quickSelect(nums, l, r, targert)


if __name__ == '__main__':
    s = Solution()
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
