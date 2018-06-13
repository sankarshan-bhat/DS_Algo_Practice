class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        isWordended=True
        prevChar=''
        res = False
        for i in range(0,len(bits)):
            if(isWordended and prevChar == '' and bits[i] == 0 ):
                #print '0 matched', bits[i],i
                if i == len(bits)-1:
                    res = True
            elif (prevChar == 1 and (bits[i]==1 or bits[i]== 0)):
                    #print '10 or 11 matched'
                    isWordended = True
                    prevChar=''
            else:
                    #print '1 found'
                    prevChar = 1
                    isWordended = False
        return res
              
                
                
            
            
        
        
        
        