# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root : 
            return []
        
        ans = []
        
        q = []
        q.append(root)
        l2r = True
        
        while len(q)!=0 :
            size = len(q)
            lvl = [0]*size
            for i in range(size):
                node = q[0]
                q=q[1:]
                if not l2r : 
                    index = size-i-1
                    lvl[index] = node.val
                else : 
                    lvl[i] = node.val
                if node.left : 
                    q.append(node.left)
                if node.right : 
                    q.append(node.right)
            l2r = not l2r 
            ans.append(lvl)
        return ans 