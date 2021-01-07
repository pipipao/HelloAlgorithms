from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def dfs(n):
            if (not n.left) and (not n.right):
                return True
            l=False
            r=False
            if n.left:
                if n.left.val<n.val:
                    l= dfs(n.left)
                else:
                    return False
            else:
                l=True
            if n.right:
                if n.right.val>n.val:
                    r=dfs(n.right)
                else:
                    return False
            else:
                r=True
            return l and r
        return dfs(root)

if __name__ == '__main__':
    s=Solution()
    root=TreeNode(2,TreeNode(1),TreeNode(3))
    s.isValidBST(root)