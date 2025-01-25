class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        s=set()
        
        for i in range(0,len(nums)):
            for j in range(i+1,len(nums)):
                k=j+1
                l=len(nums)-1
                while(k<l):
                    sums=nums[i]+nums[j]+nums[l]+nums[k]
                    if(sums==target):
                        s.add((nums[i],nums[j],nums[l],nums[k]))
                        k+=1
                        l-=1
                    elif(sums<target):
                        k+=1
                    else:
                        l-=1
        output=list(s)
        return output


                

        