class Solution(object):
    def minCost(self, n):
        dp = [0] * (n + 1)

        for x in range(2, n + 1):
            dp[x] = float('inf')
            for a in range(1, x):
                b = x - a
                dp[x] = min(dp[x], a * b + dp[a] + dp[b])

        return dp[n]