# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        self.PrintTree(root)
    
    def PrintTree(self, root: TreeNode):
        if root.left:
            self.PrintTree(root.left)
        print(root.val)
        if root.right:
            self.PrintTree(root.right)