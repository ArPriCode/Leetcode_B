class Solution:
    def stoneGameVII(self, a: List[int]) -> int:
        p = [0,*accumulate(a)]

        @lru_cache(1500)
        def f(i,j):
            if i<j:
                diff1 = p[j]-p[i]-f(i+1,j)
                diff2 = p[j-1]-p[i-1]-f(i,j-1)

                return max(diff1,diff2)
            
            return 0
        
        return f(1,len(a))