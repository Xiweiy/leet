class Solution(object):
    def canAttendMeetings(self, intervals):
        intervals = sorted(intervals, key=lambda x: (x.start,x.end))
        
        if not len(intervals)-1:
            return True
        
        for i in range(len(intervals)-1):
            start1,end1 = intervals[i].start, intervals[i].end
            start2,end2 = intervals[i+1].start, intervals[i+1].end
            if end1 > start2:
                return False
        return True

##(1) Sort by start and then end (2) compare consecutive tuples with no overlap
