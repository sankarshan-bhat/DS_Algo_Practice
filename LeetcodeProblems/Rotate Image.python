class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        
        first rotate the matrix , then swap i,j accordingly to produce the desired result
        
        """
        matrix.reverse()
        print matrix
        
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix[i])):
                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        
        