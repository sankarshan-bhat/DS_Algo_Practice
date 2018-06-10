class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        missingSum = nums[0]
        maxElement = nums[0]
        for i in range(1,len(nums)):
            missingSum += nums [i]
            if nums [i] >maxElement :
                maxElement = nums[i]
        
        originalSum = len(nums)*(len(nums) +1)/2
        
        return originalSum - missingSum