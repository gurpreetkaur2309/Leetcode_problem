# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
        
#         """
#         left=0
#         right=0
#         ni=[]
#         if(m > n):
#             for i in range(0,m):
#                 if(nums1[left] < nums2[right]):
#                     ni.append(left)
#                     left+=1
#                 else:
#                     ni.append(right)
#                     right+=1
#         else:
#             for i in range(0,n):
#                 if(nums2[left] < nums1[right]):
#                     ni.append(left)
#                     left+=1
#                 else:
#                     ni.append(right)
#                     right+=1
#         return ni


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        midx = m - 1
        nidx = n - 1 
        right = m + n - 1

        while nidx >= 0:
            if midx >= 0 and nums1[midx] > nums2[nidx]:
                nums1[right] = nums1[midx]
                midx -= 1
            else:
                nums1[right] = nums2[nidx]
                nidx -= 1

            right -= 1
        