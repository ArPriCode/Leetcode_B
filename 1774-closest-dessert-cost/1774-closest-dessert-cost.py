class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        baseCosts.sort(reverse=True)
        toppingCosts.sort(reverse=True)

        N, M = len(baseCosts), len(toppingCosts)

        answer = float('inf')

        def _recursion(cost, index):
            nonlocal answer

            if abs(target-cost) <= abs(answer-target):
                if abs(target-cost) == abs(answer-target):
                    answer = min(answer, cost)
                else:
                    answer = cost
            
            if index == M:
                return
            
            _recursion(cost, index+1)
            _recursion(cost + toppingCosts[index], index+1)
            _recursion(cost + (2*toppingCosts[index]), index+1)
        
        for i in baseCosts:
            _recursion(i, 0)
        
        return answer