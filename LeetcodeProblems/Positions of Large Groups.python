class Solution(object):
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        rcount = 1
        fList = []
        iList = []
        
        if len (S) == 0:
            return []
        s = S
        #print s,len(s),len(S)
        prev = ""
        i = 0
        while i < len(s):
            print "i:",i
            rcount = 1
            start = i 
            while i< len(s) and prev == s[i] :
                #print "matching"
                rcount +=1
                #print "rcount",rcount
                end = i
                prev = s[i]
                i +=1
                
            if rcount >= 3 : 
                #print "rcount >= 3 "
                iList = []
                iList.append(start-1)
                iList.append(end)
                fList.append(iList)
            if i < len(s):
                prev = s[i]    
            #print prev,rcount
            i +=1
            
        print fList
        return fList
            
            
        