from collections import defaultdict

class Solution(object):
    def numberOfBoomerangs(self, points):
        ans = 0

        for x1, y1 in points:
            cnt = defaultdict(int)

            for x2, y2 in points:
                dx = x1 - x2
                dy = y1 - y2
                d = dx * dx + dy * dy
                cnt[d] += 1

            for c in cnt.values():
                ans += c * (c - 1)

        return ans