class Solution:
    def maxTotal(self, value: List[int], limit: List[int]) -> int:
        buckets = defaultdict(list)
        for v, L in zip(value, limit):
            buckets[L].append(v)

        ans = 0
        for L, arr in buckets.items():
            arr.sort(reverse=True)
            ans += sum(arr[:L])
        return ans