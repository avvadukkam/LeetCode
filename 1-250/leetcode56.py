class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i=1
        while i<len(intervals):
            a, b = intervals[i-1]
            c, d = intervals[i]
            if b>=c and b<=d:
                intervals[i]= [a,d]
                intervals.pop(i-1)
            elif b>=c and b>=d:
                intervals.pop(i)
            else:
                i+=1
        return intervals