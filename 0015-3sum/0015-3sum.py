class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # # result=[]
        # # for i in range(0,len(nums)):
        # #     print(i)
        # #     for j in range(0,len(nums)):
        # #         for k in range(0,len(nums)):
        # #             if (i != j  and i != k and j != k and nums[i]+nums[j]+nums[k]==0):
                        
        # #                 l=[nums[i],nums[j],nums[k]]
        # #                 if l not in result:
        # #                     result.append(l)

        # # return result
        
        # # for an in range(0,len(nums)):
        # #     i=an
        # #     j=an
        # #     k=an
        # result=[]
        # sets=set()
        
       
        # print(nums)
        # trys=nums[0]
        # for i in range(1,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if(nums[i]+nums[j]+trys==0  ):
        #             result.append([nums[i],nums[j],trys])
        #             sets.add((nums[i],nums[j],trys))
        #             print(sets)
        # # return list(sets)
        # return result
        target=0
        nums.sort()
        s=set()
        output=[]
        for i in range(0,len(nums)):
            j=i+1
            k=len(nums)-1
            while(j<k):
                sums=nums[i]+nums[j]+nums[k]
                if(sums==target):
                    s.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
                elif(sums<target):
                    j+=1
                else:
                    k-=1
        output=list(s)
        return output
                




