class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        nums[:] = accumulate(nums)
        pf = nums
        summ = pf[-1]
        if summ == 0:
            n = len(nums)
            return (n-1)*(n-2)//2 % (10**9 + 7)

        cnt = 0
        for il in range(bisect.bisect_right(pf, summ//3)):
            p1 = bisect.bisect_left(pf, pf[il] + pf[il])
            if p1 < il+1: p1 = il+1

            p2 = bisect.bisect_right(pf, pf[il] + (summ - pf[il]) // 2 )
            cnt += p2-p1

        return cnt % (10**9 + 7)
        