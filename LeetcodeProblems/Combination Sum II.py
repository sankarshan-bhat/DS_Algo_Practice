class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        rList =[]
        candidates.sort()
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
                if i > start and nums[i] == nums[i-1]:
                    continue
                self.permuteHelper(rList,tempList+[nums[i]],nums,target,cSum+nums[i],i+1)
                #tempList.pop()
        