#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
# 返回一行字符串，表示原文。
# @param s1 string字符串一维数组 N*N的01矩阵，表示解密纸，0表示透明，1表示涂黑
# @param s2 string字符串一维数组 字符矩阵，表示密文
# @return string字符串
#
class Solution:
    def rotatePassword(self , s1 , s2 ):
        n=len(s1)
        card=set()
        res=''
        for i in range(n):
            for j in range(n):
                if s1[i][j]=='0':
                    card.add((i,j))
        for _ in range(4):
            for i in range(n):
                for j in range(n):
                    if (i,j) in card:
                        res+=s2[i][j]
            card=self.rotMat(n,card)
        return res



    def rotMat(self,n,card:set):
        newCard=set()
        for cord in card:
            x=cord[1]
            y=n-1-cord[0]
            newCard.add((x,y))
        return newCard