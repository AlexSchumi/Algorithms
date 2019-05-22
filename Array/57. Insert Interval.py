# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        flag = 0
        flag2 = 0
        if not intervals and not newInterval:
            return res
        if not intervals:
            return res.append(newInterval)
        if not newIntervals:
            return intervals

        for i in range(len(intervals)):
            if intervals[i].end >= newInterval.start: # the first position we can insert new int
                flag2 = 1
                break
            else:
                res.append(intervals[i]) # if not, append the original interval into the results

        if flag2 == 0:
            res.append(newInterval)
            return res
        # deal with new interval start
        if intervals[i].start >= newInterval.start:
            new_start = newInterval.start
        else:
            new_start = intervals[i].start

        new_end = newInterval[i].end
        # deal with new interval end
        for j in range(i, len(intervals)):
            if new_end >= intervals[j].start:
                new_end = max(new_end, intervals[j].end)
            else:
                #new_end = max(new_end, intervals[j].end)
                flag = 1
                break
        res.append(Interval(new_start, new_end))

        if flag == 1:
            res.append(intervals[j])
        for k in range(j+1, len(intervals)):
            res.append(intervals[k])

        return res

    """
    This is implementation based on youtube
    Time complexity: O(n)
    Space complexity: O(n)
    """
    """
    newInterval is a new interval to be inserted into intervals
    """
    def insert2(self, intervals, newInterval):
        if not newInterval:
            return intervals
        res = []
        i = 0
        while i < len(intervals) and intervals[i].end < newInterval.start:
            res.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i].start <= newIntervals.end:
            newInterval.start = min(intervals[i].start, newInterval.start)
            newInterval.end = max(intervals[i].end, newInterval.end)

        res.append(newInterval)

        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        return res


intervals = [[1,3],[6,9]], newInterval = [2,5]
