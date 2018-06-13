# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        valStack= []
        interStack=[(root,0)]

        while len(interStack) > 0:
            
            
            node , level = interStack.pop()
           
            if node:
              
                
                if len(valStack) < level +1 :
                    
                    valStack.insert(0,[])
               
                valStack[-(level +1)].append(node.val)
               
          
                interStack.append((node.right,level+1))
           
                interStack.append((node.left,level+1))
            

            
            
        return valStack
            
            
        
        