class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        
        # def quick_sort_in_place(arr, low, high):
        #     if low < high:
        #         p = partition(arr, low, high)
        #         quick_sort_in_place(arr, low, p - 1)
        #         quick_sort_in_place(arr, p + 1, high)

        # def partition(arr, low, high):
        #     pivot = arr[high]
        #     i = low - 1
        #     for j in range(low, high):
        #         if arr[j] < pivot:
        #             i += 1
        #             arr[i], arr[j] = arr[j], arr[i]
        #     arr[i + 1], arr[high] = arr[high], arr[i + 1]
        #     return i + 1
        
        # quick_sort_in_place(nums,0,len(nums)-1)
        # return nums
        high=len(nums)-1
        low=0

        mid=0
        def mergesort(nums,low,mid,high):
            left_arr=nums[low:mid+1]
            right_arr=nums[mid+1:high+1]
            left=0
            right=0
            merged_i=low
            while(left<len(left_arr) and right<len(right_arr)):
                if(left_arr[left]<=right_arr[right]):
                    nums[merged_i]=left_arr[left]
                    left=left+1
                else:
                    nums[merged_i]=right_arr[right]
                    right=right+1
                merged_i+=1
            while(left<len(left_arr)):
                nums[merged_i]=left_arr[left]
                left=left+1
                merged_i+=1  
            while(right<len(right_arr)):
                nums[merged_i]=right_arr[right]
                right=right+1
                merged_i+=1 
    
        def merge(nums,low,high):
            if(low>=high):
                return
            mid=(high+low)//2
            merge(nums,low,mid)
            
            merge(nums,mid+1,high)
        
            mergesort(nums,low,mid,high)


        merge(nums,low,high)
        return nums
            