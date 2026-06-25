class Solution(object):
    def mirrorReflection(self, p, q):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        g = gcd(p, q)
        l = (p * q) // g

        m = l // p
        n = l // q

        if m % 2 == 0:
            return 0
        if n % 2 == 1:
            return 1
        return 2