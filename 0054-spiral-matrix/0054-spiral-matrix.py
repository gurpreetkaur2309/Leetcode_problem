class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left=0
        right=len(matrix[0])-1
        top=0
        bottom=len(matrix)-1

        l=len(matrix)* len(matrix[0])
        print(l)
        li=[]

        count=0
        while(count<l):
            index=left
            if(count<l):
                while(index<=right):

                    li.append(matrix[top][index])
                    index+=1
                    count+=1

            top+=1
            index=top
            if(count<l):
                while(index<=bottom):
                    li.append(matrix[index][right])
                    index+=1
                    count+=1

                right-=1
                index=right
            if(count<l):
                while(index>=left):
                    li.append(matrix[bottom][index])
                    index-=1
                    count+=1

                bottom-=1
                index=bottom
            if(count<l):
                while(index>=top):
                    li.append(matrix[index][left])
                    index-=1
                    count+=1
                left+=1
                print(count)
        return li

            
            




        