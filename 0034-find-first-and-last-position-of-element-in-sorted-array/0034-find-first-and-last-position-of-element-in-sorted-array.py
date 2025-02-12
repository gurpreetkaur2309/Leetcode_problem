class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        count=0
        i=0
        end=0
        if(n==0):
            return [-1,-1]
        else:
            # while( i<n and nums[i]!=target ):
            #     i+=1
            # start=i
            # if(start>=n):
            #     return [-1,-1]
            # for loop in range(i,n):
            #     if(nums[loop]!=nums[i]):
            #         end=loop-1
            # return [start,end]
            
            
            s=[]
            for i in range(n):
                if(nums[i]==target):
                    s.append(i)
            if(len(s)==0):
                return [-1,-1]
            else:
                return [s[0],s[len(s)-1]]
            
                
        
            
                    


            
                
                
        