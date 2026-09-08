class Solution(object):
    def countCommas(self, n):
        ans = 0
        for i in range(1, n+1):
            digit = len(str(i))
            ans += (digit-1) // 3

        return ans