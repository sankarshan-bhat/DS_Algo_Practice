# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    maxLen = 0
    def longestPath(self,root):
        if not root:
            return 0
        left_s = self.longestPath(root.left)
        right_s = self.longestPath(root.right)
        
        left_a = right_a = 0
        
        if root.left and root.val == root.left.val:
            left_a = left_s +1
        if root.right and root.val == root.right.val:
            right_a = right_s +1
        
        self.maxLen = max(self.maxLen,left_a+right_a)
        return max(left_a,right_a)
            
        
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None :
            return 0 
        else:
            self.longestPath(root)
            
        return self.maxLen
        
        
        
    