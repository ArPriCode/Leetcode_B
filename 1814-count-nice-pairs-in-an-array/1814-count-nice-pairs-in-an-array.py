class Solution:
    def reverseNumber(self, num: int) -> int:
        return int(str(num)[::-1])

    def countNicePairs(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        count = 0
        mp = defaultdict(int)

        for i in range(len(nums)):
            nums[i] = nums[i] - self.reverseNumber(nums[i])

        for num in nums:
            count = (count + mp[num]) % MOD
            mp[num] += 1

        return count