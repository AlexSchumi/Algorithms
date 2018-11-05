## This is my implementation for merging intervals
class Interval(object):
    def __init__(self, s, e):
        self.start = s
        self.end = e

def merge(intervals):
    """
    :type intervals: List[intervals]
    :rtype: List[intervals]
    """
    if not intervals and len(intervals) == 1:
        return intervals
    # otherwise, sort intervals in ascending order by starting point
    intervals.sort(key=lambda x: x.start)

    res = [] # return res
    j = 0

    for i in range(1, len(intervals)):
        cnt = 0 # record how many intervals we have merged
        j = i-1
        inter = intervals[j]
        while intervals[i].start <= inter.end:
            inter =  Interval(inter.start, intervals[i].end)
            i += 1
            cnt += 1
        # the end of merge procedures
        if cnt >= 1:
            res.append(inter)
        else:
            res.append(intervals[i])
        i += 1
    return res


def mymerge2(intervals):
    """
    :type intervals: List[intervals]
    :rtype: List[intervals]
    """
    if not intervals or len(intervals) == 1:
        return intervals
    res = []
    intervals.sort(key=lambda x: x.start)
    s = intervals[0].start
    e = intervals[0].end
    for inter in intervals:
        if inter.start <= e:
            e = max(inter.end, e)
        else:
            res.append(Interval(s, e)) # append merged interval in results
            s = inter.start
            e = inter.end
    res.append(Interval(s, e))
    return res






a1 = Interval(1, 3)
a2 = Interval(2, 6)
a3 = Interval(8, 10)
a4 = Interval(15, 18)
interval = [a1, a3, a4, a2]
print(interval[1].start)
interval.sort(key=lambda x: x.start)
print(interval[1].start)

print(mymerge2(interval)[2].end)
