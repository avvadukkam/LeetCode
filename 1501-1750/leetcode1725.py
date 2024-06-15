class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        min_side = []
        for sides in rectangles:
            min_side.append(min(sides))
        res = max(min_side)
        return min_side.count(res)