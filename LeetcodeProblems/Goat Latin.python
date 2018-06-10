class Solution(object):
    def isVowel(self,char):
        return char.lower() in "aeiou"
    
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str
        """
        worldList = S.split(" ")
        count = 0
        OutputStr = "" 
        for i in range (len(worldList)): 
             count  +=1
             if len(worldList[i]) > 0:
                    char = worldList[i][0]
                    if self.isVowel(char):
                        OutputStr += worldList[i] + "ma" + "a"*count
                    else:
                        lchar = worldList[i][0]
                        OutputStr += worldList[i][1:] + lchar+ "ma" + "a"*count
             if i < len(worldList)-1:            
                OutputStr += " "    
        print OutputStr
        return OutputStr 
             