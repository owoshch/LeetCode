#Attempted on Tue, 23 Jan 2018. Didn't manage to solve in 20 minutes.
# Decided to reveal the solution.


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# started 8:13am

# [[[0, 30],[5, 10],[15, 20]]]
# [0 [5 10] [15 20] 30]
# [0 [5 10]]
# [0 [5 10] [15 20] 30]
# [0]
# min = 0, opened = 1
# max = 30, opened = 1, needed = 1
# 5 > min
# [0 5 10 15 20 30]

# [[[0, 30],[5, 10],[15, 20]]]
# [0 [5 10] [15 20] 30]
# # [0 [5 10] [15 20] [25 30] 35]

# starts = 0
# ends = 0, n = 1
# 5 > starts, 10 < ends n += 1
# open = [0, 5]
# close = [10, 30]

# 15. open = [0, 5, 15]
# 20. open = [10, 20, 30]


class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        
