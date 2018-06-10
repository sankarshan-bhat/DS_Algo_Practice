class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rList =[]
        nums.sort()
        self.subsetsWithDupHelper(rList,[],nums,0)
        return rList
        
    def subsetsWithDupHelper(self,rList,tempList,nums,start):
        
        rList.append(tempList)
        #print rList
        
        for i in xrange(start, len(nums)):
            #tempList.append(nums[i])
            #if not (nums[i] == nums[i-1]):
            if i > start and  nums[i] == nums[i-1]:
                continue
            self.subsetsWithDupHelper(rList,tempList+[nums[i]],nums,i+1)
            #tempList.pop()
            
            
        
        