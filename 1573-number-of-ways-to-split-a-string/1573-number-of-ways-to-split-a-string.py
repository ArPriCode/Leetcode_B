class Solution(object):
    def numWays(self, s):
        MOD = 10**9 + 7
        n = len(s)

        total = s.count('1')

        if total == 0:
            return ((n - 1) * (n - 2) // 2) % MOD

        if total % 3 != 0:
            return 0

        k = total // 3

        cnt = 0
        first = second = 0

        for ch in s:
            if ch == '1':
                cnt += 1

            if cnt == k:
                first += 1
            elif cnt == k + 1:
                break

        cnt = 0
        for ch in s:
            if ch == '1':
                cnt += 1

            if cnt == 2 * k:
                second += 1
            elif cnt == 2 * k + 1:
                break

        return (first * second) % MOD