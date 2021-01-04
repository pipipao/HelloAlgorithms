# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def check(self,a,b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        return a.val==b.val and self.check(a.left,b.right) and self.check(a.right,b.left)
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.check(root,root)