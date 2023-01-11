# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            if not p and not q:
                return True
            
            return False
        
        p_qu = []
        q_qu = []
        p_qu.append(p)
        q_qu.append(q)

        while p_qu or q_qu:
            ptemp = p_qu.pop(0)
            qtemp = q_qu.pop(0)

            if ptemp.val != qtemp.val:
                return False
            
            if ptemp.left or qtemp.left:
                if ptemp.left and qtemp.left:
                    p_qu.append(ptemp.left)
                    q_qu.append(qtemp.left)
                
                else:
                    return False
            
            if ptemp.right or qtemp.right:
                if ptemp.right and qtemp.right:
                    p_qu.append(ptemp.right)
                    q_qu.append(qtemp.right)
                
                else:
                    return False

        return True
