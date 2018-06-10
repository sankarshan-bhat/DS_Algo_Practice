# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
count = 0
class Solution(object):
    '''
    def countPathUtil(self,root,sum):
        res = 0
        
        if root == None  :
            return res
        if root.val == sum:
            res += 1
            print root.val
             
        
        
        
        res += self.countPathUtil(root.left,sum-root.val) 
        res += self.countPathUtil(root.right,sum-root.val)
        
        return res
        
       
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        
        if root == None :
            print "returning 0"
            return 0 
        else:
            print "in else"
            return self.countPathUtil(root,sum) + self.countPathUtil(root.left,sum) + self.countPathUtil(root.right,sum)
    '''
    def pathSum(self, root, s):
        return self.helper(root, s, [s])

    def helper(self, node, origin, targets):
        if not node: return 0
        hit = 0
        for t in targets:
            if not t-node.val: hit += 1                          # count if sum == target
        #print"for node.val",node.val,
        #print "hits",hit
        targets = [t-node.val for t in targets]+[origin]         # update the targets
        #print "target",targets
        return hit+self.helper(node.left, origin, targets)+self.helper(node.right, origin, targets)
        
        