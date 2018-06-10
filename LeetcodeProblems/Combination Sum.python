class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        rList =[]
        self.permuteHelper(rList,[],candidates,target,0,0)
        return rList
    
    def permuteHelper(self,rList,tempList,nums,target,cSum,start):
        #print "tempList",tempList
        if cSum == target:
            rList.append(tempList)
        elif cSum > target:
            return
            
        else:
            for i in xrange(start, len(nums)):
                self.permuteHelper(rList,tempList+[nums[i]],nums,target,cSum+nums[i],i)
                #tempList.pop()
        