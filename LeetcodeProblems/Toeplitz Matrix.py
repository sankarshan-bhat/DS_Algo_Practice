class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(0,len(matrix)-1):
            for j in range(len(matrix[0])-1,-1,-1):
                print i,j
                print matrix[i][j]
                if(j+1 <= len(matrix[0])-1):
                    print matrix[i+1][j+1]
                    if (matrix[i][j] != matrix[i+1][j+1]):
                        return False
        return True
                #if(i+1<len(matrix[0])):
        