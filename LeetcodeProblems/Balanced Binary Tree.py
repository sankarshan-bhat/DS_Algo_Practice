# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getHeight(self,node):
        if node == None:
            return 0
        return 1+ max(self.getHeight(node.left),self.getHeight(node.right))
    
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        
        lheight = self.getHeight(root.left)
        rheight = self.getHeight(root.right)
        
        if abs(rheight - lheight) > 1:
            return False
        
        return self.isBalanced(root.left ) and self.isBalanced(root.right)
        
        
        