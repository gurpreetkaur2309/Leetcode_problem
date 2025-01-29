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
        intervals.sort(key = lambda x:x[0])
        a=[]
        for i in range(len(intervals)):
            if not a or a[-1][1] < intervals[i][0]:
                a.append(intervals[i])
            else:
                a[-1][1]= max(a[-1][1],intervals[i][1])

        return a





        