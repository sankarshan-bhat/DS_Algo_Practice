class Solution(object):
    
    def generatePermutation(self,string,index,result):
        if  index == len(string)-1:
            return
        
        
        
        
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = ['']
        for i in range(len(S)):
            ch = S[i]
            if ch.isalpha():
                res = [sol+ch.lower() for sol in res] + [sol+ch.upper() for sol in res]
                #print res
            else:
                
                res = [sol+ch for sol in res ]
                
        return res
        