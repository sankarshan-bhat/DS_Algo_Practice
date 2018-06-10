# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if (root):
            return self.checkSymmetric(root.left,root.right)
        else:
            return True
    
    def checkSymmetric(self,nleft,nright):
        if nleft == None and nright:
            return False
        
        if nleft and nright == None :
            return False
        
        if nleft == None and nright == None:
            return True
        
        
        return nleft.val == nright.val and self.checkSymmetric(nleft.left,nright.right) and self.checkSymmetric(nleft.right,nright.left)
        