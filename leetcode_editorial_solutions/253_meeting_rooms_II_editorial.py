# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e




class Solution:
    def minMeetingRooms(self, intervals):
            """
            :type intervals: List[Interval]
            :rtype: int
            """
            starts = []
            ends = []
            for i in range(len(intervals)):
                starts.append(intervals[i].start)
                ends.append(intervals[i].end)
            starts = sorted(starts)
            ends = sorted(ends)
            end_index = 0
            rooms_required = 0
            for i in range(len(starts)):
                if starts[i] < ends[end_index]:
                    rooms_required += 1
                else:
                    end_index += 1
            return rooms_required
