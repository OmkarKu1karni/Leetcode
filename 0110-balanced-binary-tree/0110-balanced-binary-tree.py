# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def height(root):
    if not root : 
        return 0
    lh = height(root.left)
    rh = height(root.right)
    
    return max(lh,rh)+1

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root : 
            return True 
        lh = height(root.left)
        rh = height(root.right)
        
        if abs(lh-rh)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right) :
            return True
        return False