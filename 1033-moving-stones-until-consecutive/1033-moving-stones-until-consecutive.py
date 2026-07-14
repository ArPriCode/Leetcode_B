class Solution(object):
    def numMovesStones(self, a, b, c):
        stones = [a, b, c]
        stones.sort()

        diff1 = (stones[1] - stones[0]) - 1
        diff2 = (stones[2] - stones[1]) - 1

        non_zero = []

        if diff1 > 0:
            non_zero.append(diff1)
        if diff2 > 0:
            non_zero.append(diff2)
        
        non_zero.sort()

        mini = maxi = 0

        if len(non_zero) == 2:
            mini, maxi = non_zero
        elif len(non_zero) == 1:
            maxi = non_zero[-1] 

        if not non_zero:
            return [
                0, mini + maxi
            ]
        
        one_true = True if 1 in non_zero else False
        
        return [
            min(len(non_zero), 1 if one_true else 2),
            mini + maxi
        ]