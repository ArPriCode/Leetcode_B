from functools import lru_cache
from typing import List

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        @lru_cache(None)
        def dfs(left, right):
            # [left, right) contains only one stone
            if right - left == 1:
                return 0

            ans = 0

            for i in range(left + 1, right):
                leftSum = prefix[i] - prefix[left]
                rightSum = prefix[right] - prefix[i]

                if leftSum < rightSum:
                    ans = max(ans, leftSum + dfs(left, i))

                elif leftSum > rightSum:
                    ans = max(ans, rightSum + dfs(i, right))

                else:
                    ans = max(
                        ans,
                        leftSum + max(
                            dfs(left, i),
                            dfs(i, right)
                        )
                    )

            return ans

        return dfs(0, n)