class Solution:
    def singleNumber(self, nums: list()) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res


if __name__ == '__main__':
    i = Solution.singleNumber(Solution, [1, 1, 2])
    print(i)
