class Solution:
    def findMin(self, nums: List[int]) -> int:
        mins=nums[0]
        for i in range(len(nums)):
            if(nums[i]<mins):
                mins=nums[i]
        return mins
        