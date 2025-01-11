class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min=prices[0]
        index=0
        if(len(prices)>1):
        #     for i in range(0,len(prices)):
        #         if(prices[i]<min):
        #             min=prices[i]
        #             index=i
        #             print(index)
        #     max=prices[index]
        #     for i in range(index,len(prices)):

        #         if(prices[i]>max):
        #             max=prices[i]
        #     return max-min
            max=prices[0]
            min=prices[0]
            # for i in range(0,len(prices)-1):
            #     for j in range(i+1,len(prices)):
            #         if(prices[j]-prices[i]>max):
            #             max=prices[j]-prices[i]
            # return max
            arr=[]
            for i in range(0,len(prices)):
                if(prices[i]<min):
                    arr.append(max-min)
                    min=prices[i]
                    max=prices[i]
                elif(prices[i]>max):
                    max=prices[i]
            arr.append(max-min)
            max=arr[0]
            for i in arr:
                if(i>max):
                    max=i
            return max




        else:
            return 0

        