class Solution(object):
    def sumAndMultiply(self, n):
        digits = [int(d) for d in str(n) if d != '0']
        
        if not digits:
            return 0
        
        x = int(''.join(map(str, digits)))
        s = sum(digits)
        
        return x * s