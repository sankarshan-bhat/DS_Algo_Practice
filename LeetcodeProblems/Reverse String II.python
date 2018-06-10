class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        begin=0
        i=0
        rString=""
        tempStr=""
        while i<len(s):
            if(k>(len(s)-i)):
                tempStr = s[i:len(s)]
                #print ">k"+tempStr
                rString += tempStr[::-1]
                #print rString
            elif((2*k)>(len(s)-i) and (len(s)-i) >=k):
                tempStr = s[i:i+k]
                #print "k to 2*k"+tempStr
                rString += tempStr[::-1]
                #print rString
                rString += s[i+k:len(s)]
            else:
                tempStr = s[i:i+k]
                #print tempStr
                rString += tempStr[::-1]
                rString +=s[i+k:i+(2*k)]
                #print rString
            i=i+(2*k)
            
        return rString
            
            
            
            
            
            
        