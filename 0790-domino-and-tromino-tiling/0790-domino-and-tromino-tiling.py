class Solution:
    def numTilings(self, n: int) -> int:
        return (f:=cache(lambda i:i>2 and (2*f(i-1)+f(i-3))%(10**9+7) or (1,1,2)[i]))(n)