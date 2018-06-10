# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

noList = []
class Solution(object):
    
    def sumNumbersHelper(self,root,cSum):
        if root == None:
            
            return 0
        elif root.left == None and root.right == None:
            print"adding csum", cSum+root.val
            return cSum +root.val
        else:
            cSum = (cSum+root.val)*10

        return self.sumNumbersHelper(root.left,cSum)+ self.sumNumbersHelper(root.right,cSum)

        
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        
        return self.sumNumbersHelper(root,0)
        
        