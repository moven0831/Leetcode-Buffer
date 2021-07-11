# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:            
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack_left = [root.left]
        stack_right = [root.right]
        
        while len(stack_left) > 0 and len(stack_right) > 0:
            left =  stack_left.pop()
            right =  stack_right.pop()
            if not left and not right:
                continue
            elif not left or not right:
                return False
            
            if left.val != right.val:
                return False
            stack_left.append(left.left)
            stack_left.append(left.right)
            stack_right.append(right.right)
            stack_right.append(right.left)
        return len(stack_left) == 0 and len(stack_right) == 0