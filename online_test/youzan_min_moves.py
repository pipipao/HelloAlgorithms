#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 最少移动次数
# @param nums int整型一维数组
# @return int整型
#
class Solution:
    def minMoves(self , nums ):
        mins=sum(nums)
        maxn=max(nums)
        minn=min(nums)
        for i in range(minn,maxn+1):
            step=0
            for n in nums:
                step+=abs(n-i)
            if step<=mins:
                mins=step
        return mins
if __name__ == '__main__':
    s=Solution()
    print(s.minMoves([1,2,4]))