class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l=0
        r=len(matrix)-1
        while(l<r):
            for i in range(0,r-l):
                top,bottom=l,r
                top_left=matrix[top][l+i]
                matrix[top][l+i]=matrix[bottom-i][l]
                matrix[bottom-i][l]=matrix[bottom][r-i]
                matrix[bottom][r-i]=matrix[top+i][r]
                matrix[top+i][r]=top_left
                print(matrix)
            
            r-=1
            l+=1
            



        