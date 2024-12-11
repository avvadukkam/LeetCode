class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_dist = 0
        n = len(colors)

        for i in range(n):
            if colors[i] != colors[0]:
                max_dist = max(max_dist, i)

        for i in range(n):
            if colors[i] != colors[n-1]:
                max_dist = max(max_dist, n-i-1)

        return max_dist