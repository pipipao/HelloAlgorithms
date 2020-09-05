#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# @param arr int整型一维数组
# @param k int整型 允许0变为1的个数
# @return int整型
#
class Solution:
    def GetMaxConsecutiveOnes(self, arr, k):
        if not arr:
            return 0
        length=len(arr)
        maxl=0
        for left in range(length):
            leftk=k
            right=left
            flag=True
            while flag:
                if right<length:
                    if arr[right]==1:
                        right+=1
                    elif leftk>0:
                        right+=1
                        leftk-=1
                    else:
                        clen=right-left
                        if clen>maxl:
                            maxl=clen
                        flag=False
                else:
                    clen = right - left
                    if clen > maxl:
                        maxl = clen
                    break
        return maxl

if __name__ == '__main__':
    s=Solution()
    print(s.GetMaxConsecutiveOnes([1,1,1,0,0,0,1,1,1,1,0],2))




