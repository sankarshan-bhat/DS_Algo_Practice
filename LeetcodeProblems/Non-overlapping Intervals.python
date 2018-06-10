# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if len(intervals) < 1: 
            return 0
        intervals = sorted(intervals, key=lambda x:(x.start))
        curEnd = intervals[0].end
        count = 0
        for i in range(1,len(intervals)):
            if intervals[i].start < curEnd: 
                count += 1
                curEnd = min (intervals[i].end, curEnd)
            else :
                curEnd = intervals[i].end
        return count
            
                