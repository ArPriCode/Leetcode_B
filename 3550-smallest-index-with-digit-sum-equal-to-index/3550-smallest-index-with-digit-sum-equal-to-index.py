class Solution(object):
    def smallestIndex(self, nums):
        for i in range(len(nums)):
            s = sum(int(d) for d in str(nums[i]))
            if s == i:
                return i
        return -1