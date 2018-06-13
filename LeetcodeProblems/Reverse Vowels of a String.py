class Solution(object):
    def swapVowels(self,strVal,voWelList):
        strList = list(strVal)
        low = 0
        high = len(voWelList) -1
        
        while(low < high):
            #print s[voWelList[low]],s[voWelList[high]]
            strList[voWelList[low]],strList[voWelList[high]] = strList[voWelList[high]],strList[voWelList[low]]
            low = low +1
            high = high -1
        return ''.join(strList)
        
        
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        prevVowelIndex = -1
        voWelList=[]
        print s
        s=s.encode('utf-8')
        for i in range(0,len(s)):
            if(s[i] =='a' or s[i] =='e'or s[i] =='i' or s[i] =='o' or s[i] =='u' or s[i] =='A' or s[i] =='E'or s[i] =='I' or s[i] =='O' or s[i] =='U'):
                    print s[i]
                    voWelList.append(i)
             
        return self.swapVowels(s,voWelList)
                    
                    
                    
                    
            
            
        