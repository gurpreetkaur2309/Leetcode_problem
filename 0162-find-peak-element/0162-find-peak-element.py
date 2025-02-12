class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        maxs=nums[0]
        n=len(nums)
        index=0
        for i in range(n):
            if(nums[i]>maxs):
                maxs=nums[i]
                index=i
        return index
              