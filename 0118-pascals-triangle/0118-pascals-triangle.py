class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # first=1
        # second=1
        # l1=[]
        # if(numRows==1):
        #      l1.append([1])
        # elif(numRows==2):
        #     l1.append([1])
        #     l1.append([1],[1,1])
        # else:
        #     l1.append([1])
        #     l1.append([1,1])
        #     for i in range(2,numRows):
        #         k=[]
               
        #         for j in range(0,i+1):
        #               k.append(1)
        #               k[-1]=1
        #               print(l1)
        #               print(k)
        #             #   k.append( l1[i-1][c]+l1[i-1][c+1])
        #             #   c=c+1
        #         l1.append(k)
        pascal = []
        
        for i in range(numRows):
            # Start with a row of 1s
            row = [1] * (i + 1)
            # Update the inner values of the row, excluding the edges
            for j in range(1, i):  # Skip the first and last element
                row[j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
            # Add the row to the Pascal's Triangle
            pascal.append(row)
        
        return pascal
        # arr=[]
        # if(numRows==1):
        #     arr.append([1])
        #     return arr
        # if(numRows==2):
        #     arr.append([1])
        #     arr.append([1,1])
        #     return arr
        # elif(numRows>2):
        #     for i in range(2,numRows):
        #         arr1=[0]*(i+1)
        #         arr1[0]=1
        #         arr1[i]=1
                
        #         a=1
        #         index=1
        #         temp=arr[i-1]
        #         a+=1
        #         for j in range(0,len(temp)-1):

        #             arr1[index]=temp[j]+temp[j+1]
        #             index+=1
        #         print(arr1)
        #         arr.append(arr1)
        # return arr
                    
                    
        