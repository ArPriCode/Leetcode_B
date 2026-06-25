class Solution(object):
    def countMajoritySubarrays(self, nums, target):
        n = len(nums)
        size = 2 * n + 5
        bit = [0] * size
        offset = n + 2

        def update(idx, val):
            while idx < size:
                bit[idx] += val
                idx += idx & -idx

        def query(idx):
            s = 0
            while idx > 0:
                s += bit[idx]
                idx -= idx & -idx
            return s

        prefix = 0
        ans = 0

        update(offset, 1)

        for x in nums:
            if x == target:
                prefix += 1
            else:
                prefix -= 1

            idx = prefix + offset
            ans += query(idx - 1)
            update(idx, 1)

        return ans