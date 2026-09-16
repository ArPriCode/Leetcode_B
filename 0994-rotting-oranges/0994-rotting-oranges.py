from collections import deque
class Solution:
    def orangesRotting(self, nums: List[List[int]]) -> int:
        grid = nums.copy()
        m,n = len(nums), len(nums[0])
        ans, fresh = 0, 0
        que = deque()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    que.append([i, j])

        if fresh == 0 :
            return 0
        
        while que:
            ans += 1
            for _ in range(len(que)):
                i,j = que.popleft()
                if i-1 >= 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    fresh -= 1
                    que.append([i-1, j])
                if i+1 < m and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    fresh -= 1
                    que.append([i+1, j])
                if j-1 >= 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    fresh -= 1
                    que.append([i, j-1])
                if j+1 < n and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    fresh -= 1
                    que.append([i, j+1])

        return ans-1 if fresh == 0 else -1