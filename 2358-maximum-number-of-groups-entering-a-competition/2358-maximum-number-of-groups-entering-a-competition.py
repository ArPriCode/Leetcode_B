class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        
        x = len(grades)
        n = 0.5 * ((8 * x + 1) ** 0.5 - 1)
        ans = int(n)
        
        return ans