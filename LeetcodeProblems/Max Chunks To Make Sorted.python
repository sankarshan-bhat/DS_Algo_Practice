class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        
        maxSoFar = MaxChunk = 0
        
        for index,val in enumerate(arr):
            maxSoFar = max(maxSoFar,val)
            
            if maxSoFar == index:
                MaxChunk += 1
                
        return MaxChunk
        