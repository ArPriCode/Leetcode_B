class Solution:
    def areSentencesSimilar(self, s: str, t: str) -> bool:
        s, t = s.split(), t.split()
        k1 = sum(takewhile(int, map(eq, s, t)))
        k2 = sum(takewhile(int, map(eq, s[::-1], t[::-1])))

        return k1 + k2 >= min(len(s), len(t))