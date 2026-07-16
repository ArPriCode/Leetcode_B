class Solution(object):
    def secondsBetweenTimes(self, startTime, endTime):
        def time_to_seconds(time_str):
            h, m, s = map(int, time_str.split(':'))
            return h * 3600 + m * 60 + s
        
        return time_to_seconds(endTime) - time_to_seconds(startTime)