# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def getdiameter(root,diameter):
        if not root : 
            return 0
        
        lh = getdiameter(root.left , diameter)
        rh = getdiameter(root.right , diameter)
        
        diameter[0] = max(diameter[0],lh+rh)
        
        return 1+max(lh,rh)
    
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = [0]
        getdiameter(root,diameter)
        return diameter[0]
    
    
        