class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prevCount=0
        curCount=1
        res=0
        for i in range(1 , len(s)):
            if s[i]==s[i-1]:
                curCount=curCount+1
            else:
                prevCount=curCount
                curCount=1
            if prevCount >= curCount:
                res=res+1
        return res
            
        