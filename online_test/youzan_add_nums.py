#
#
# @param num int整型 相加的数字
# @param itemNum int整型 相加项数
# @return long长整型
#
class Solution:
    def sum(self , num , itemNum ):
        res=0
        p=num
        for _ in range(itemNum):
            res+=num
            num*=10
            num+=p
        return res


if __name__ == '__main__':
    s=Solution()
    print(s.sum(3,5))