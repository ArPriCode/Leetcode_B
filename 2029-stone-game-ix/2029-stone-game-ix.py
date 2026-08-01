class Solution(object):
    def stoneGameIX(self, stones):
        c0 = c1 = c2 = 0
        for v in stones:
            r = v % 3
            if r == 0:
                c0 += 1
            elif r == 1:
                c1 += 1
            else:
                c2 += 1

        if c1 == 0 and c2 == 0:
            return False

        if c0 % 2 == 0:
            return c1 > 0 and c2 > 0

        return abs(c1 - c2) > 2