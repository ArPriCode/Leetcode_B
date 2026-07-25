class Solution(object):
    def maxProduct(self, n):
        digits = [int(d) for d in str(n)]
        max1 = max2 = 0
        for num in digits:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num
        return max1 * max2