# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda x: x.start)
        merged = []
        for interval in intervals:
            """
            If the list of merged intervals is empty or if the current
            interval does not overlap with the previous, appent it:
            """
            if not merged or merged[-1].end < interval.start:
                merged.append(interval)
            else:
                # there is an overlap, merge the current and previous
                # intervals
                merged[-1].end = max(merged[-1].end, interval.end)
        return merged