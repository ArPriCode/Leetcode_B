class Solution:
    def numMovesStonesII(self, stones: List[int]) -> List[int]:
        
        stones.sort()
        n, left, lo = len(stones), 0, inf

        hi = max(stones[n-1]-stones[1], stones[n-2]-stones[0]) - n + 2
        
        for right in range(n):

            left= bisect_right(stones,stones[right]-n)

            if right-left == stones[right]-stones[left] == n-2: lo = min(lo, 2)
            
            else: lo = min(lo, n - (right-left+1))

        return [lo, hi]