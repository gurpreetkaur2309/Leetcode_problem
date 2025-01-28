# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
#         l=[]
#         i=-1
#         while(i<len(intervals)-2):
#            i+=1
#            f= intervals[i][0]
#            s= intervals[i][1]
#            print(i)
           
#            if(s>= intervals[i+1][0]):
#             l.append([f,intervals[i+1][1]])
#             i=i*2
#             print(i)
#            else:
#             l.append([f,s])
           
        
#         return l
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals by their start times
        intervals.sort(key=lambda x: x[0])
        
        merged = []
        
        for interval in intervals:
            # If merged is empty or current interval does not overlap
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Overlap case: merge intervals
                merged[-1][1] = max(merged[-1][1], interval[1])
        
        return merged




        