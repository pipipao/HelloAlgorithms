class Interval:
    def __init__(self, a=0, b=0):
        self.start = a
        self.end = b

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回Interval类，start代表汪仔最少做对了多少道题，end代表汪仔最多做对了多少道题。
# @param n int整型 选择题总数
# @param k int整型 朋友做对的题数
# @param str1 string字符串 长度为n只包含ABCD的字符串，其中第i个代表汪仔第i题做出的选择
# @param str2 string字符串 长度为n只包含ABCD的字符串，其中第i个代表朋友第i题做出的选择
# @return Interval类
#
class Solution:
    def solve(self , n , k , str1 , str2 ):
        me=str1
        friend=str2
        same=0
        for i in range(n):
            if me[i]==friend[i]:
                same+=1
        notSame=n-same
        max=0
        min=0
        if k>same:
            max=n-(k-same)
            if k<=notSame:
                min=0
            else:
                min=k-notSame
        else:#k<=same
            if k<=notSame:
                min=0
            else:
                min=k-notSame
            wrong=n-k
            if wrong>notSame:
                max=n-(wrong-notSame)
            else:
                max=n

        res=Interval(min,max)
        return res


if __name__ == '__main__':
    s=Solution()
    res=s.solve(3,0,"ABC","ABC")
    print(res.start,res.end)