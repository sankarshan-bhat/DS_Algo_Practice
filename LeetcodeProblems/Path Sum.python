# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathUtil(self,root,currentSum,sum):
        if root and root.left == None  and root.right == None and (currentSum+root.val) == sum:
            return True
        elif root == None or (root.left == None  and root.right == None and (currentSum+root.val) != sum):
            return False
        
        return self.hasPathUtil(root.left,(currentSum+root.val),sum) or self.hasPathUtil(root.right,(currentSum+root.val),sum)
        
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None or (root == None and sum == 0) :
            return False 
        else:
            return self.hasPathUtil(root,0,sum)
        