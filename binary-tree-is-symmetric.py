# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool: 
        def left_right_check(left, right):
            if left and right:  
                if left.val == right.val:
                    return left_right_check(left.left, right.right) and \
        left_right_check(left.right, right.left) 
                else: return False
            else:
                if left or right: return False
                return True            
        
        return left_right_check(root.left, root.right)
        