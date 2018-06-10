class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charDict = {}
        rLen = 0 
        maxlen = 0
        subStr = ""
        for i in range(0,len(s)):
            
            cChar = s[i]
            if cChar in subStr:
                #print "char in -1",s[i]
                subStr = s[charDict[s[i]]+1 :i+1]
                
            
            else:
                #print "char in -curCharCount >= 0",s[i]    
                subStr +=cChar
                #print "rLen in curCharCount >= 0 ",rLen
            charDict[s[i]] = i   
            maxlen = max(maxlen,len(subStr))    
           
                    
        return maxlen