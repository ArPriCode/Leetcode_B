from heapq import heappush, heappop

class Solution(object):
    def findSafeWalk(self, grid, health):
        m, n = len(grid), len(grid[0])

        dist = [[float('inf')] * n for _ in range(m)]
        start = grid[0][0]
        dist[0][0] = start

        pq = [(start, 0, 0)]
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while pq:
            cost, x, y = heappop(pq)

            if cost != dist[x][y]:
                continue

            if x == m - 1 and y == n - 1:
                return cost < health

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    ncost = cost + grid[nx][ny]
                    if ncost < dist[nx][ny]:
                        dist[nx][ny] = ncost
                        heappush(pq, (ncost, nx, ny))

        return False