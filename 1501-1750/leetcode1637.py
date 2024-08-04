class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = sorted(set(point[0] for point in points))
        
        if len(x) < 2:
            return 0
        
        max_width = max(x[i+1] - x[i] for i in range(len(x) - 1))
        
        return max_width