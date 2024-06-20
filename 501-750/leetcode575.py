class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        diff_candy = len(set(candyType))
        max_allowed = len(candyType)//2
        return max_allowed if max_allowed < diff_candy else diff_candy