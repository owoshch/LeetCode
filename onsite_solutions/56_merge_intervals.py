"""
June 8, 2018
30 minutes. 
Fails for the case:
Input: [[5,5],[1,3],[3,5],[4,6],[1,1],[3,3],[5,6],[3,3],[2,4],[0,0]]
Expected output: [[0,0],[1,6]]
My output: [[0,0],[1,3],[4,6]]
"""


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def overlap(self, first_interval, second_interval, begin, end):
        if begin == -1 and end == -1:
            begin = first_interval.start
            end = first_interval.end
        return max(begin, second_interval.start) <= min(end, second_interval.end)
    
    
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda x: x.start)
        
        result = []
        if len(intervals) == 0:
            return result
        begin, end = -1, -1
        i, j = 0, 1
        while j < len(intervals):            
            while j < len(intervals) and self.overlap(intervals[i], intervals[j], begin, end):
                begin = min(intervals[i].start, intervals[j].start)
                end = max(intervals[i].end, intervals[j].end)
                j += 1
            if begin != -1 and end != -1:
                result.append(Interval(begin, end))
                begin = -1
                end = -1
            else:
                result.append(intervals[i])
            i = j
            j += 1
        if i < len(intervals):
            result.append(intervals[i])
        return result