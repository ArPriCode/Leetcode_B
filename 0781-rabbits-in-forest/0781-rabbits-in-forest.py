class Solution(object):
    def numRabbits(self, answers):
        count = {}

        for x in answers:
            count[x] = count.get(x, 0) + 1

        ans = 0

        for x, c in count.items():
            group = x + 1
            ans += ((c + group - 1) // group) * group

        return ans