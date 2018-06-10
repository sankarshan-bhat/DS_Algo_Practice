class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rList =[]
        self.subsetsWithDupHelper(rList,[],nums,0)
        return rList
    
    def subsetsWithDupHelper(self,rList,tempList,nums,start):
        rList.append(tempList)
        
        for i in xrange(start, len(nums)):
            #tempList.append(nums[i])
            self.subsetsWithDupHelper(rList,tempList+[nums[i]],nums,i+1)
            #tempList.pop()
            
        
        