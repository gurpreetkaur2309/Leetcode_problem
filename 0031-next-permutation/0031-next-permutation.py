class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # if(len(nums)>1):
        #     temp=0
        #     for i in range(len(nums)-1,1,-1):
        #         if(nums[i]>nums[i-1]):
        #             swap=nums[i-1]
        #             nums[i-1]=nums[i]
        #             nums[i]=swap
        #             temp=1
        #             print(nums)
        #             break
        #     if(temp==0):
        #         if(nums[0]<nums[1]):
        #             nums.sort(reverse=True)
        #         else:
        #             nums.sort()
        n = len(nums)
        idx = -1

        # Step 1: Find the first decreasing element from the right
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                idx = i
                break

        if idx == -1:
            # Array is in descending order, reverse to get smallest permutation
            nums.reverse()
            return nums

        # Step 2: Find the element to swap with nums[idx]
        for i in range(n - 1, idx, -1):
            if nums[i] > nums[idx]:
                nums[i], nums[idx] = nums[idx], nums[i]
                break

        # Step 3: Reverse the subarray nums[idx+1:]
        nums[idx + 1:] = reversed(nums[idx + 1:])
        


# Dry Run Example


            
           
        

        