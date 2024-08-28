# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfsheight(root):
    if root == None:
                return 0
    lh = dfsheight(root.left)
    if lh==-1 :
        return -1
    rh = dfsheight(root.right)
    if rh==-1 :
        return -1
    if abs(lh-rh)>1 :
        return -1
    return 1+max(lh,rh)
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return dfsheight(root)!=-1
