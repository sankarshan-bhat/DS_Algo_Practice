class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xorall = nums[0]
        setbits=[]
        notsetbits=[]
        rList=[]
        for i in range (1,len(nums)):
            xorall = xorall ^ nums[i]
        
        rightMostSet = xorall & ~(xorall-1)
        
        for i in range  (0,len(nums)):
            if rightMostSet & nums[i]:
                setbits.append(nums[i])
            else:
                notsetbits.append(nums[i])
        
        num1=setbits[0]
        for i in range  (1,len(setbits)):
            num1 = num1 ^ setbits[i]
        
        rList.append(num1)
            
        num2=notsetbits[0]
        for i in range  (1,len(notsetbits)):
            num2 = num2 ^ notsetbits[i]
        
        rList.append(num2)
        
        return rList
        
        
        
            
        
        
        