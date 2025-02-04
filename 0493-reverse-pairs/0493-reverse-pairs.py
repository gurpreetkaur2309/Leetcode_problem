# class Solution:
#     def reversePairs(self, nums: List[int]) -> int:
        # n=len(nums)
        # count=0
        # nums.sort()
        # # for i in range(0,n-1):
        # #     for j in range(i+1,n):
        # #         if(nums[i] > 2* nums[j]):
        # #             count+=1
        # left=0
        # right=n-1
        # for i in range(0,n):
        #     if(nums[])
                    
        # return count
class Solution:
    def reversePairs(self, nums):
        def countPairs(nums, low, mid, high):
            nonlocal count
            j = mid + 1
            for i in range(low, mid + 1):
                while j <= high and nums[i] > 2 * nums[j]:
                    j += 1
                count += (j - (mid + 1))  # Count valid pairs

        def mergesort(nums, low, mid, high):
            nonlocal count
            
            # Count reverse pairs before merging
            countPairs(nums, low, mid, high)

            # Normal merge process
            left_arr = nums[low:mid + 1]
            right_arr = nums[mid + 1:high + 1]
            
            left = 0
            right = 0
            merged_i = low

            while left < len(left_arr) and right < len(right_arr):
                if left_arr[left] <= right_arr[right]:
                    nums[merged_i] = left_arr[left]
                    left += 1
                else:
                    nums[merged_i] = right_arr[right]
                    right += 1
                merged_i += 1

            while left < len(left_arr):
                nums[merged_i] = left_arr[left]
                left += 1
                merged_i += 1  

            while right < len(right_arr):
                nums[merged_i] = right_arr[right]
                right += 1
                merged_i += 1 
        
        def merge(nums, low, high):
            if low >= high:
                return
            mid = (high + low) // 2
            merge(nums, low, mid)
            merge(nums, mid + 1, high)
            mergesort(nums, low, mid, high)

        count = 0  
        merge(nums, 0, len(nums) - 1)
        return count
