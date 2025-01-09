
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hello=[]
        for i in nums:
            if i==0:
                hello.append(i)
        for i in nums:
            if i==1:
                hello.append(i)
        for i in nums:
            if i==2:
                hello.append(i)
        print(hello)
        for i in range(0,len(nums)):
            nums[i]=hello[i]

        
            

        
        