from collections import defaultdict

class Solution(object):
    def minScore(self, n, roads):
        graph = defaultdict(list)

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        visited = set([1])
        stack = [1]
        ans = float('inf')

        while stack:
            node = stack.pop()

            for nei, wt in graph[node]:
                ans = min(ans, wt)
                if nei not in visited:
                    visited.add(nei)
                    stack.append(nei)

        return ans