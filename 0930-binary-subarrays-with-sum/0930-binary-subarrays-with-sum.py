class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.atmostK(nums, goal) - self.atmostK(nums, goal - 1)
    
    def atmostK(self, nums: List[int], goal: int) -> int:
        i = j = 0
        total_sum = 0
        count = 0

        while i < len(nums):
            total_sum += nums[i]

            while j <= i and total_sum > goal:
                total_sum -= nums[j]
                j += 1
            count += i - j + 1
            i += 1
        
        return count