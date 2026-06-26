class Solution(object):
    def sampleStats(self, count):
        total = sum(count)
        s = 0

        mn = -1
        mx = -1
        mode = 0
        modeFreq = 0

        for i in range(256):
            if count[i]:
                if mn == -1:
                    mn = i
                mx = i
                s += i * count[i]

                if count[i] > modeFreq:
                    modeFreq = count[i]
                    mode = i

        mean = float(s) / total

        if total % 2:
            k1 = k2 = total // 2 + 1
        else:
            k1 = total // 2
            k2 = k1 + 1

        cur = 0
        m1 = m2 = 0

        for i in range(256):
            cur += count[i]

            if cur >= k1 and m1 == 0:
                m1 = i

            if cur >= k2:
                m2 = i
                break

        median = (m1 + m2) / 2.0

        return [float(mn), float(mx), mean, median, float(mode)]