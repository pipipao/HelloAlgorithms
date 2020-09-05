#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# @param matrix int整型二维数组
# @return int整型一维数组
#
class Solution:
    def SpiralMatrix(self, matrix):
        if not matrix:
            return None
        ylen = len(matrix[0])
        xlen = len(matrix)
        x = y = 0
        check = set()
        left, right, up, down = False, False, False, False
        right = True
        ans = []
        ans.append(matrix[x][y])
        check.add((0,0))
        while len(check) < (xlen * ylen):
            if right:
                if y + 1 >= ylen or (x, y+1) in check:
                    right = False
                    down = True
                else:
                    y += 1
                    ans.append(matrix[x][y])
                    check.add((x, y))
            if down:
                if x + 1 >= xlen or (x+1, y) in check:
                    down = False
                    left = True
                else:
                    x += 1
                    ans.append(matrix[x][y])
                    check.add((x, y))
            if left:
                if y - 1 < 0 or (x, y-1) in check:
                    left = False
                    up = True
                else:
                    y -= 1
                    ans.append(matrix[x][y])
                    check.add((x, y))
            if up:
                if x - 1 < 0 or (x-1, y) in check:
                    up = False
                    right = True
                else:
                    x -= 1
                    ans.append(matrix[x][y])
                    check.add((x, y))
        return ans


if __name__ == '__main__':
    s = Solution()

    print(s.SpiralMatrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
