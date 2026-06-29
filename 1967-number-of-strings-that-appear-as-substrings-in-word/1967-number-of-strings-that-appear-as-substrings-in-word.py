class Solution(object):
    def numOfStrings(self, patterns, word):
        ans = 0
        for s in patterns:
            if s in word:
                ans += 1
        return ans