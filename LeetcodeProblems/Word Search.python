class Solution(object):
    def SearchWord(self,board,rowIndex,colIndex,word,wordIndex):
        if rowIndex >=len(board) or colIndex >= len(board[0]) or rowIndex < 0 or colIndex < 0 or wordIndex > len(word)-1 or word[wordIndex] != board[rowIndex][colIndex]:
            return False
        if wordIndex == len(word) -1 and board[rowIndex][colIndex] == word[wordIndex]:
            #board[rowIndex][colIndex] = '#'
            #print "word  char matched found",word[wordIndex],rowIndex,colIndex
            return True
        previuosChar = board[rowIndex][colIndex] 
        #if board[rowIndex][colIndex] == word[wordIndex]:
        board[rowIndex][colIndex] = '#'
        #print "word  char matched found",word[wordIndex],rowIndex,colIndex
        res = self.SearchWord(board,rowIndex+1,colIndex,word,wordIndex+1) or self.SearchWord(board,rowIndex-1,colIndex,word,wordIndex+1) or self.SearchWord(board,rowIndex,colIndex+1,word,wordIndex+1) or self.SearchWord(board,rowIndex,colIndex-1,word,wordIndex+1)
        board[rowIndex][colIndex] = previuosChar
        return res
        
        
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board :
            return False
        res = False
        for i in range (0, len(board)):
            for j in range (0,len(board[0])):
                if self.SearchWord(board,i,j,word,0):
                     res=True
                '''
                #if board[i][j] == word[0] and i+1 < len(board) and j+1 < len(board[0]) and i-1 >=0 and j-1 >= 0:
                if board[i][j] == word[0] :
                    board[i][j] = '#'
                    print "first word found",word[0],i,j 
                    if len(word) > 1:
                        res = self.SearchWord(board,i+1,j,word,1) or self.SearchWord(board,i-1,j,word,1) or self.SearchWord(board,i,j+1,word,1) or self.SearchWord(board,i,j-1,word,1)
                    else:
                        res = True
                    
                if res ==  True :
                    return res
                '''
        return res
        