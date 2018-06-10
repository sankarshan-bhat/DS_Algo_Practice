class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        isPrefix = True
        finalStr= ""
        cIndex= 0
        if len(strs) == 0:
            return ""
        for i in range(len(strs[0])):
            c = strs[0][i]
            #print "char",c
            for j in range(1,len(strs)):
                #print "inside 2 loop"
                if cIndex >= len(strs[j]):
                    #print "cIndex > len(strs[j])"
                    isPrefix = False
                if cIndex < len(strs[j]) and strs[j][cIndex] != c:
                     #print "cIndex < len(strs[j]) and strs[j][cIndex] != c"
                     isPrefix = False
                    
            cIndex +=1
            if isPrefix:
                finalStr += c
                
        return finalStr
        