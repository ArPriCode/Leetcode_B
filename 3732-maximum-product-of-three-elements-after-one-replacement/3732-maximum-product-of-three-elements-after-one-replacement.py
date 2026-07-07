class Solution(object):
    def maxProduct(self, nums):
        nums.sort()
        n = len(nums)
        ll = nums[n - 1] * nums[n - 2] * 100000
        ll = max(ll, nums[0] * -100000 * nums[n - 1])
        ll = max(ll, nums[0] * nums[1] * 100000)
        return ll