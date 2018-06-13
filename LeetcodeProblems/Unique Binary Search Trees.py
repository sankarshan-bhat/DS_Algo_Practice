class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        T = [0]*(n+1)
        print T
        T[0] =1 
        T[1] =1 
        if n >= 1:
            
        
            for i in range(2,n+1):
                for j in range(0,i):
                    T[i] += T[j]*T[i-j-1]
        print T        
        return T[n]
        