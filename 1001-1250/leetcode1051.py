class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        current = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                current += 1
        return current