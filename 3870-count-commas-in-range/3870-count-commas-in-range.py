class Solution:
    def countCommas(self, n: int) -> int:
        inte=str(n)
        if len(inte)<4:
            return 0
        else:
            a=(len(inte)-1)//3
            print(a)
            ans= n - (1000 ** a) + 1
            print(ans)
            return ans
