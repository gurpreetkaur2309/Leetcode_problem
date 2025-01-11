class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        even=0
        odd=1
        arr=[0]*len(nums)
        for i in nums:
            if (i>0):
                arr[even]=i
                print(even)
                even+=2
            else:
                arr[odd]=i
                odd+=2
        return arr
             