class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod=-2147483648
        mul=1
        # for i in range(0,len(nums)):
        #     mul=1
        #     mul=mul* nums[i]
        #     if(mul > max_prod):
        #         max_prod=mul
        # for i in range(0,len(nums)-1):
        #     mul=1
        #     for j in range(i,len(nums)):
        #         mul=mul* nums[j]
        #         if(mul > max_prod):
        #             max_prod=mul
        # return max_prod
        pre=1
        s=1
        n=len(nums)
        for i in range(0,len(nums)):
            if(pre==0):
                pre=1
            if(s==0):
                s=1
            pre=pre*nums[i]
            s=s*nums[n-i-1]
            max_prod=max(max_prod,max(pre,s))
            # if(pre>s):
            #     mul=pre
            # else:
            #     mul=s
        return max_prod

                
            

        