class Interval(object):
    def __init__(self, s, e):
        self.start = s
        self.end = e

def meetingroom(intervals): # This is my wrong first version
    """
    :type intervals: List[intervals]
    :rtype: int
    """
    if not intervals:
        return 0
    if len(intervals) == 1:
        return 1
    res = len(intervals) # num of meeting room is equal to the length of intervals
    # Whenever we found a non-overlap intervals, res -= 1
    intervals.sort(key=lambda x: x.start)  # sort by the starting time
    #s = intervals[0].start
    e = intervals[0].end
    for inter in intervals:
        if inter.start < e: # overlap in the meeting time
            e = min(e, inter.end)
            #s = max(s, inter.start)
        else:
            res -= 1
            e = inter.end
            #s = inter.start
    return res


def meetingroom2(intervals): # This is my corrrect first version
    """
    :type intervals: List[intervals]
    :rtype: int
    """
    if not intervals:
        return 0
    if len(intervals) == 1:
        return 1
    res = 0
    intervals.sort(key=lambda x: x.start)  # sort by the starting time
    ends = []

    for inter in intervals:
        s = inter.start
        idx = find_index(ends, s)
        if idx == None: # no ending time is less than start time
            ends.append(inter.end)
            res += 1 # create a new room
        else:
            ends[idx] = inter.end
    return res


def find_index(alist, val):
    if alist:
        if all(val < x for x in alist): # all starting time is less than ending time, create a new room
            return None
        else:
            return [n for n, x in enumerate(alist) if val > x][0]
    else: # if alist is None
        return None # ancillary function for meetingroom2


def meetingroom3(intervals): ## This is youtube video implementation
    if not intervals:
        return 0
    if len(intervals) == 1:
        return 1
    starts = []
    ends = []
    res = 0
    for inter in intervals:
        starts.append(inter.start)
        ends.append(inter.end)
    starts.sort()
    ends.sort()

    j = 0
    e = ends[j]
    for i in range(len(starts)):
        if starts[i] < e:
            res += 1
        else: # starts[i] >= e, we can use the same room
            j += 1
            e = ends[j] # move to the next ends time
    return res


a1 = Interval(0, 10)
a2 = Interval(8, 12)
a3 = Interval(11, 25)
a4 = Interval(13, 18)
a5 = Interval(2, 4)
interval = [a1, a2, a3, a4]
print(meetingroom3(interval))
