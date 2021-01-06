from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        lenx=len(board)
        leny=len(board[0])
        lenWord=len(word)
        def dfs(index,used,x,y):
            if x<0 or x>=lenx or y<0 or y>=leny:
                return False
            if board[x][y]!=word[index]:
                return False
            if (x,y) in used:
                return False
            if index==lenWord-1:
                return True
            temp=used.copy()
            temp.add((x,y))
            if dfs(index+1,temp,x,y-1) or dfs(index+1,temp,x-1,y) or dfs(index+1,temp,x,y+1) or dfs(index+1,temp,x+1,y):
                return True
            return False
        for startX in range(lenx):
            for startY in range(leny):
                if dfs(0,set(),startX,startY):
                    return True
        return False

# backtrack
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def check(i: int, j: int, k: int) -> bool:
            if board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            visited.add((i, j))
            result = False
            for di, dj in directions:
                newi, newj = i + di, j + dj
                if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
                    if (newi, newj) not in visited:
                        if check(newi, newj, k + 1):
                            result = True
                            break

            visited.remove((i, j))
            return result

        h, w = len(board), len(board[0])
        visited = set()
        for i in range(h):
            for j in range(w):
                if check(i, j, 0):
                    return True

        return False

if __name__ == '__main__':
    s=Solution()
    s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB")
