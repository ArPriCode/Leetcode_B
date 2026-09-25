class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        self.memo = {}
        return self._solve(coins, amount)
        
    def _solve(self, coins, rem):
        if rem < 0:
            return -1
        if rem == 0:
            return 0
        if rem in self.memo:
            return self.memo[rem]
        
        min_count = float('inf')
        
        for coin in coins:
            res = self._solve(coins, rem - coin)
            if res != -1:
                min_count = min(min_count, 1 + res)
        
        self.memo[rem] = min_count if min_count != float('inf') else -1
        return self.memo[rem]