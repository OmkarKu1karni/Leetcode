# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root : 
            return []
        ans = []
        q = []
        q.append(root)
        while len(q)!=0:
            size = len(q)
            lvl = []
            for i in range(size) : 
                node = q[0]
                q=q[1:]
                lvl.append(node.val)
                if node.left : 
                    q.append(node.left)
                if node.right :
                    q.append(node.right)
            ans.append(lvl)
        return ans 
                