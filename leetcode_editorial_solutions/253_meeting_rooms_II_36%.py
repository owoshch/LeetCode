# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


# beats 36% of submissions


class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        starts = []
        ends = []
        for meeting in intervals:
            starts.append(meeting.start)
            ends.append(meeting.end)
        starts.sort()
        ends.sort()
        rooms_required = 0
        rooms_available = 0
        start_index = 0
        end_index = 0
        while start_index < len(starts):
            if starts[start_index] < ends[end_index]:
                if not rooms_available:
                    rooms_required += 1
                else:
                    rooms_available -= 1
                start_index += 1
            else: #next meeting began
                rooms_available += 1
                end_index += 1
        return rooms_required
