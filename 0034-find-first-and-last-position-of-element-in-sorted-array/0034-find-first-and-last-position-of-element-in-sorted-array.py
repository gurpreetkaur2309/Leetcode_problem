class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        if(n==0):
            return [-1,-1]
        else:
            s=[]
            for i in range(n):
                if(nums[i]==target):
                    s.append(i)
            if(len(s)==0):
                return [-1,-1]
            else:
                return [s[0],s[len(s)-1]]
            
                
        
            
                    


            
                
                
        