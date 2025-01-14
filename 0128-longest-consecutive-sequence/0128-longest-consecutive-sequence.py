class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if(len(nums)>=1):
            nums=list(set(nums))
            nums.sort()
            count=0
            start=nums[0]
            arr=[]
            
            for i in nums:
                if(i==start):
                    count+=1
                    start+=1
                    print(i)
                else:
                    arr.append(count)
                    count=1
                    start=i
                    start+=1
                arr.append(count)
                
            max=arr[0]
            for i in arr:
                if i > max:
                    max=i

            return max
        else:
            return 0

        