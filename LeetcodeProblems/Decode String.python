class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        rstack  = []
        curString ='';cNum =0 ;prevString = '' 
        for i in range(len(s)):
            if s[i].isdigit():
                cNum = cNum*10 + int(s[i])
            elif s[i] == '[':
                rstack.append(curString)
                rstack.append(cNum)
                
                cNum = 0 
                curString = ''
                
            elif s[i] == ']':
                num = rstack.pop()
                prevString = rstack.pop()
                curString = prevString + curString* num
            else:
                curString += s[i]
        return curString
                