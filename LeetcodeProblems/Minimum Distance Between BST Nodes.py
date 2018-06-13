# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    prevVal = -1
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        minValList=[]
        minValList.append(100000)
        return self.findMinValInTree(root,minValList)
        '''
        print "Lmin ",lMin
        rMin = self.findMinValInTree(root.right,root,minValList)
        print "rMin" , rMin
        if lMin == None :
            return rMin
        elif rMin == None:
            return lMin
        else:
            return min(lMin,rMin)
        '''
        
    
    def findMinValInTree(self,root,minValList):
        if root == None :
            return
      
       
        
        #print "minVal Found",minValList[0]
        
        self.findMinValInTree(root.left, minValList)
        print "excuting with",root.val,minValList[0]
        if self.prevVal != -1 :
            minValList[0] = min(abs (root.val - self.prevVal),minValList[0])
        
        self.prevVal = root.val
        
        self.findMinValInTree(root.right,minValList)
        
        return minValList[0]
            
        
        
        
        