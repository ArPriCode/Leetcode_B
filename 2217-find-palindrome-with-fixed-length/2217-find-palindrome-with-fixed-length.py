class Solution(object):
    def kthPalindrome(self, queries, intLength):
        """
        :type queries: List[int]
        :type intLength: int
        :rtype: List[int]
        """
        res = []
        half_len = (intLength + 1) // 2
        start = 10 ** (half_len - 1)
        total = 9 * start  

        for q in queries:
            if q > total:
                res.append(-1)
                continue

            half = str(start + q - 1)
            pal = half + half[-2::-1] if intLength % 2 else half + half[::-1]
            res.append(int(pal))
        return res