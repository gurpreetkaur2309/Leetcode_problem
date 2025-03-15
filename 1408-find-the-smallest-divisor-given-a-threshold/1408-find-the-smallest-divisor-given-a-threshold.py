class Solution:
    
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # check=nums[0]
        # for i in nums:
        #     if()
        # for i in range(0,len(nums)):
        #     ans=0
        #     for j in range(0,len(nums)):
        #         ans=ans+(j/i)
        left, right = 1, max(nums)
        def division_sum(divisor):
            return sum(math.ceil(num / divisor) for num in nums)

        
        while left < right:
            mid = (left + right) // 2
            if division_sum(mid) > threshold:
                left = mid + 1
            else:
                right = mid

        return left
    
            


        