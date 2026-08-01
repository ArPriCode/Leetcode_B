from fractions import Fraction

class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        cnt = Counter(Fraction(w, h) for w, h in rectangles)
        return sum(v*(v-1)//2 for v in cnt.values())