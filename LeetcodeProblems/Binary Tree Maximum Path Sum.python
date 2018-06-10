# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    maxVal = -1000000000
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.helper(root)
        return self.maxVal
    def helper(self,root):
        if  not root:
            return 0
        
        left = max(self.helper(root.left),0)
        right = max(self.helper(root.right),0)
        
        self.maxVal = max (self.maxVal,root.val+left+right)
        
        return root.val + max(left,right)
        
            
        