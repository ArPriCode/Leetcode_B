class Solution(object):
    def solveEquation(self, equation):
        def parse(expr):
            coef = 0
            const = 0
            i = 0
            n = len(expr)

            while i < n:
                sign = 1
                if expr[i] == '+':
                    i += 1
                elif expr[i] == '-':
                    sign = -1
                    i += 1

                num = 0
                hasNum = False
                while i < n and expr[i].isdigit():
                    num = num * 10 + int(expr[i])
                    i += 1
                    hasNum = True

                if i < n and expr[i] == 'x':
                    if not hasNum:
                        num = 1
                    coef += sign * num
                    i += 1
                else:
                    const += sign * num

            return coef, const

        left, right = equation.split('=')

        lcoef, lconst = parse(left)
        rcoef, rconst = parse(right)

        coef = lcoef - rcoef
        const = rconst - lconst

        if coef == 0:
            if const == 0:
                return "Infinite solutions"
            return "No solution"

        return "x=" + str(const // coef)