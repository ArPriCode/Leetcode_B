class Solution(object):
    def totalHammingDistance(self, nums):
        n = len(nums)
        ans = 0

        for b in range(32):
            ones = 0
            for x in nums:
                if (x >> b) & 1:
                    ones += 1
            ans += ones * (n - ones)

        return ans