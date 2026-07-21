class Solution(object):
    def flipLights(self, n, presses):
        if n == 0:
            return 0
        if presses == 0:
            return 1
        if n == 1:
            return 2
        if n == 2:
            return 3 if presses == 1 else 4
        if presses == 1:
            return 4
        elif presses == 2:
            return 7
        else:
            return 8