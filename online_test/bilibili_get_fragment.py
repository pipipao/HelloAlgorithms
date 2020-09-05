#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# @param str string字符串
# @return int整型
#
class Solution:
    def GetFragment(self, str):
        if not str:
            return 0
        check=set()
        num=0
        for i in range(len(str)):
            if i>0 and str[i]==str[i-1]:
                continue
            elif str[i] in check:
                num+=1
            else:
                check.add(str[i])
        show=num+len(check)
        return int(len(str)/show)

