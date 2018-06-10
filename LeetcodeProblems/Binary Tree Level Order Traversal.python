# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = []
        fList = [[]]
        level =0 
        if root == None:
            return []
        queue.append((root,0))
        while len(queue) > 0 :
            node,level = queue.pop(0)
            print "level",level
            print node.val
            items = fList[level] if len(fList) > level else None
            if items == None:
                fList.insert(level,[node.val])
            else:
                fList[level].append(node.val)  
         
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level+1))
                      
        print  fList
        return fList
            
                      
            