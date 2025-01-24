class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dictionary={}
        arr=[]
        count=0
        dictionary[nums[0]]=count
        n=len(nums)
        for i in range(n):
            
            
            if nums[i] in dictionary:
                count=dictionary[nums[i]]
                count+=1
                dictionary[nums[i]]=count
            else:
                dictionary[nums[i]]=1
        print(dictionary)
        for i in dictionary:
            if(dictionary[i] > (n/3)):
                arr.append(i)
        return arr




        