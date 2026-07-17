class Solution(object):
    def smallestNumber(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0

        if num < 0:
            return -int("".join(sorted(str(-num), reverse=True)))

        digits = sorted(str(num))
        if digits[0] == '0':
            for i, d in enumerate(digits):
                if d != '0':
                    digits[0], digits[i] = digits[i], digits[0]
                    break

        return int("".join(digits))