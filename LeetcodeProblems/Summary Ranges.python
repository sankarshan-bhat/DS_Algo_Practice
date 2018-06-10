class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        i=0
        reslist= []
        resStr=""
        isPrevEndseen= False
        if len(nums) > 0 :
            startNum = nums[0]
        while i < len(nums): 
            if(i+1) == len(nums) and not(isPrevEndseen):
                 reslist.append(str(startNum))
                 break
            elif (i+1) == len(nums) and isPrevEndseen:
                 endNum = nums[i]
                 reslist.append(str(startNum)+"->"+str(endNum))
                 break
            if(nums[i]+1 != nums[i+1] ):
                if not(isPrevEndseen):
                    endNum=nums[i]
                    reslist.append(str(startNum))
                    print "adding to list with single",str(startNum)
                    startNum = nums[i+1]
                    isPrevEndseen= False
                else:
                    endNum=nums[i]
                    reslist.append(str(startNum)+"->"+str(endNum))
                    print "adding to list start and end ",str(startNum)+"->"+str(endNum)
                    startNum = nums[i+1]
                    isPrevEndseen= False
                   
            
            elif(nums[i]+1 == nums[i+1]):
                print "end appended", nums[i]
                endNum=nums[i]
                isPrevEndseen= True
            i=i+1
        return reslist
                 
            
            
    
        