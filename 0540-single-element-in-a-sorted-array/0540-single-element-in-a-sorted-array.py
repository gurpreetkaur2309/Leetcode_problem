class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left=0
        right=1
        n=len(nums)
        for i in range(0,n-1,2):
            if(nums[i]!=nums[i+1]):
                return nums[i]
        return nums[n-1]

            # 
            
          
        