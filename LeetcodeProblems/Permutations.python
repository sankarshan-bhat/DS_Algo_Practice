class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        rList =[]
        self.permuteHelper(rList,[],nums)
        return rList
    
    def permuteHelper(self,rList,tempList,nums):
        #print "tempList",tempList
        if len(tempList) == len(nums):
            rList.append(tempList)
        else:
        
            for i in xrange(0, len(nums)):
                if nums[i] in tempList:
                    continue
                self.permuteHelper(rList,tempList+[nums[i]],nums)
                #tempList.pop()