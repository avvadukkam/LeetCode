class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        min_side = []
        for sides in rectangles:
            min_side.append(min(sides))
        res = max(set(min_side), key = min_side.count)
        return min_side.count(res)