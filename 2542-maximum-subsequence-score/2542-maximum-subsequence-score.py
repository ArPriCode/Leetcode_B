class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res, prefix_sum, min_heap = 0, 0, []
        s = sorted(list(zip(nums1, nums2)), key=itemgetter(1), reverse=True)
        for i, j in s:
            prefix_sum += i
            heapq.heappush(min_heap, i)
            if len(min_heap) == k:
                x = prefix_sum * j
                res = res if res > x else x
                prefix_sum -= heapq.heappop(min_heap)
        return res