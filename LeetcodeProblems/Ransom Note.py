class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        countArr={}
        for nChar in ransomNote:
                countArr[nChar]=countArr.get(nChar,0)+1
                
                
        for cMag in magazine:
             countArr[cMag]=countArr.get(cMag,0)-1
            
        
        for key,val in countArr.iteritems():
            if(val > 0):
                return False;
            
        return True
                
            
        
        