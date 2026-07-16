class Solution(object):
    def minimumCost(self, nums, k):
        MOD = 10**9 + 7
        total_cost = 0
        total_ops = 0
        current_resources = k
        
        for num in nums:
            if current_resources < num:
                deficit = num - current_resources
                x = (deficit + k - 1) // k
                
                cost = x * (2 * total_ops + x + 1) // 2
                
                total_cost += cost
                total_ops += x
                current_resources += x * k
            
            current_resources -= num
            
        return total_cost % MOD