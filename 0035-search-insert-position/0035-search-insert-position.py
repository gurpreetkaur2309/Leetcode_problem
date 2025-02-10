class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if(nums[i]==target):
        #         return i
        start=0
        ans =len(nums)
        n=len(nums)
        end=n
        
        if(target>nums[n-1]):
            return ans
        elif(target<nums[0]):
            return 0
        else:
            for i in range(start,end):
                mid=(start+end) //2
                if(nums[mid]<target):
                    start=mid+1
                    
                elif((nums[mid]>target)):
                    ans=mid
                    end=mid-1
                elif((nums[mid]==target)):
                    return mid
            return ans
            

