class Solution(object):
    def dayOfYear(self, date):
        year = int(date[:4])
        month = int(date[5:7])
        day = int(date[8:])

        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        ans = sum(days[:month - 1]) + day

        if (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)) and month > 2:
            ans += 1

        return ans