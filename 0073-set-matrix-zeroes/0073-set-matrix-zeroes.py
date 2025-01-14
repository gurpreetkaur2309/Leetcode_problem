class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        even=[]
        odd=[]
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
                if(matrix[i][j]==0):
                    even.append(i)
                    odd.append(j)
        
       
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[0])):
    
            
                if(i in even or j in odd):
                    matrix[i][j]=0

            
        
        
                
        