class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        if A == B:
            return True
        
        for i in range(0,len(A)):
            rStr= A[i+1:len(A)]+A[0:i+1]
            print rStr
            if rStr == B :
                return True
        return False
        