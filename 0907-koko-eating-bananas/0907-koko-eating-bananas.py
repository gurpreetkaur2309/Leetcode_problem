class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        s=0
        h1=0
        f1=0.0
        n=len(piles)
        low=1
        
        piles.sort()
        high=piles[n-1]
        
        
        def gogo(piles,mid):
            h1=0
            f1=0.0
            for i in range(0,n):
                if(piles[i]/mid > piles[i]//mid):
                    h1=h1+(piles[i]//mid)+1

                else:
                    h1=h1+(piles[i]//mid)
        
            # for i in range(0,n):
            #     h1=h1 + math.ceil(piles[i] / mid )
                
            return h1
        while(low<=high):
            mid=(low+high)//2
            ans=gogo(piles,mid)
            
            if(ans<=h):
                s=mid
                high=mid-1
            else:
                low=mid+1
        return s
        