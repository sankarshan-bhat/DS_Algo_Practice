# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        valStack= []
        interStack=[(root,0)]
        avgList = [1.0]*0

        while len(interStack) > 0:
            
            
            node , level = interStack.pop()
           
            if node:
              
                
                if len(valStack) < level +1 :
                    
                    valStack.append([])
               
                valStack[level].append(node.val)
                
                
          
                interStack.append((node.right,level+1))
           
                interStack.append((node.left,level+1))
            
        print valStack
        for i,llist in enumerate(valStack):
                sumel= 0
                noel = 0 
                for index in range(len(llist)):
                    sumel += llist[index]
                    noel += 1
                avgList.append(float(sumel*1.0/noel))
            

            
            
        return avgList
        