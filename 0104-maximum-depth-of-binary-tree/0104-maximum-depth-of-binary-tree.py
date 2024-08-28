# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root : 
            return 0
        q=[]
        ans = 0 
        q.append(root)
        while len(q)!=0 :
            size = len(q)
            for i in range(size):
                node = q[0]
                q=q[1:]
                if node.left : 
                    q.append(node.left)
                if node.right :
                    q.append(node.right)
            
            ans+=1
        return ans