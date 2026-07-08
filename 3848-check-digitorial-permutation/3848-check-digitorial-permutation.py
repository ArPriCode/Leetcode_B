class Solution(object):
    def isDigitorialPermutation(self, n):
         return sorted(str(n)) in (['1'], ['2'], ['1','4','5'], ['0','4','5','5','8'])
