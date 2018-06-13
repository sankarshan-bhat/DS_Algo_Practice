class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 1: 
            return True
        
        i=len(nums)-2
        isPos = True
        while(i >=0):
            
            if (nums[i] == 0):
                
                minSkipNum=1
                isPos = False 
                i=i-1
                while i >= 0:
                   
                    
                    if(nums[i] > minSkipNum):
                        isPos = True
                        break
                    
                    minSkipNum +=1
                    i=i-1
                
            i= i-1
        return isPos
                    
                    
            
                
            
            
        