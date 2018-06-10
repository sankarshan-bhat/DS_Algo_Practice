# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        nList = []
        if root == None:
            return nList
        level = 1
        nQueue = []
        nQueue.append((root,level))
        curLevel = 0
        while( len(nQueue) != 0):
            
            node, level = nQueue.pop(0)
            if curLevel != level:
                nList.append(node.val)
                curLevel = level

            if node.right:
                nQueue.append((node.right,level+1))
            if node.left:
                nQueue.append((node.left,level+1))
        print nList
        
        return nList
            
            
        