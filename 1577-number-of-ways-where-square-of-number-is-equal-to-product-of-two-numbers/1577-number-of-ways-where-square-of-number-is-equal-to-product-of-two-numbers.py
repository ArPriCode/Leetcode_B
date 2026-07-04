from collections import Counter

class Solution(object):
    def numTriplets(self, nums1, nums2):

        def count(a, b):
            freq = Counter(b)
            ans = 0

            for x in a:
                target = x * x

                for y in freq:
                    if target % y:
                        continue

                    z = target // y

                    if z not in freq:
                        continue

                    if y == z:
                        ans += freq[y] * (freq[y] - 1) // 2
                    elif y < z:
                        ans += freq[y] * freq[z]

            return ans

        return count(nums1, nums2) + count(nums2, nums1)