class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        eleDict = {}
        countArray = [None]*len(answers)
        for i in range(len(answers)):
            if not(eleDict.get(answers[i])):
                    print "putting first time 1"
                    eleDict[answers[i]] = 1 
                    countArray[i] = 1
            elif eleDict.get(answers[i]) >=1 :
                
                 if eleDict.get(answers[i])  == answers[i]  and answers[i] ==1 :
                    print "putting eleDict.get(answers[i])  == answers[i]  and answers[i] ==1"
                    countArray [i] = eleDict.get(answers[i])+1
                    eleDict[answers[i]] = 0
                    print  countArray [i],  eleDict[answers[i]]
                    
                 elif eleDict.get(answers[i]) -1 == answers[i] and answers[i] !=1:
                    countArray [i] = 1
                    eleDict[answers[i]] = 1 
                 else:
                    countArray [i] = eleDict.get(answers[i])+1
                    eleDict[answers[i]] = eleDict.get(answers[i]) + 1
                 '''
                 if eleDict.get(answers[i])+1 <= answers[i] :
                    #print "putting eleDict.get(answers[i])+1 <= answers[i] "
                    countArray [i] = eleDict.get(answers[i])+1
                    eleDict[answers[i]] = eleDict.get(answers[i]) + 1
                 '''
                
                
       
        res=0
        print countArray
        for i in range(len(answers)):
            if countArray [i] == 1:
                res += answers[i]+1

           
        return res
                
                
                
                
        