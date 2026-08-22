class Solution:
    def minSideJumps(self, A: List[int]) -> int:
        
        # 1
        N = len(A) - 1        
        dp = [1, 0, 1]
        
        # 2
        for i in range(1, N):
            for j in range(3):
                
                # 3
                if j+1 == A[i]:
                    dp[j] = float('inf')
                else:
                    dp[j] = min(
                        dp[0] + (1 if j != 0 else 0) + (float('inf') if A[i] == 1 else 0),
                        dp[1] + (1 if j != 1 else 0) + (float('inf') if A[i] == 2 else 0),
                        dp[2] + (1 if j != 2 else 0) + (float('inf') if A[i] == 3 else 0),
                    )
                    
        # 4
        return min(dp)