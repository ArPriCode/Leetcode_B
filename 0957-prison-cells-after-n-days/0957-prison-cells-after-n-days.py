class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        curr = [0] * 8
        n = n % 14 if n % 14 != 0 else 14
        
        for _ in range(n):
            for i in range(1, 7):
                curr[i] = 1 if cells[i - 1] == cells[i + 1] else 0
            cells = curr.copy()
            
        return cells