# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathUtil(self,root,currentSum,sum,ilist,flist):
        #print ilist,flist
        if root and root.left == None  and root.right == None and (currentSum+root.val) == sum:
            ilist.append(root.val)
            flist.append(ilist)
            ilist = []
            #print "make ilost []",ilist
            
            return 
        elif root == None or (root.left == None  and root.right == None and (currentSum+root.val) != sum):
            return

        #print "before recu"
        #print ilist
        self.hasPathUtil(root.left,(currentSum+root.val),sum,ilist+[root.val],flist) 
        self.hasPathUtil(root.right,(currentSum+root.val),sum,ilist+[root.val],flist)
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        flist = []
        
        if root == None or (root == None and sum == 0) :
            return [] 
        else:
            self.hasPathUtil(root,0,sum,[],flist)
            return flist
        