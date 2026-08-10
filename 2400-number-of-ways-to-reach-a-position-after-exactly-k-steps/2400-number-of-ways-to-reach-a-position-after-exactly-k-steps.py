MOD = 10**9 + 7
class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        diff = abs(startPos - endPos)
        if k<diff:
            return 0
        if k==diff:
            return 1
        n = k+1 
        dp_pre = [0]*n 
        dp_pre[(k-diff)//2] = 1
        for _ in range(k):
            dp = [0]*n
            for i in range(n):
                if i>0:
                    dp[i] = (dp[i] + dp_pre[i-1])%MOD
                if i<n-1:
                    dp[i] = (dp[i] + dp_pre[i+1])%MOD
            dp_pre = dp
        return dp[(k+diff)//2]