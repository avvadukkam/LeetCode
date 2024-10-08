# 1st solution
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        n = len(grid)
        xy = sum(1 for row in grid for val in row if val > 0)
        xz = sum(max(row) for row in grid)
        yz = 0
        for i in range(n):
            temp = 0
            for j in range(n):
                temp = max(grid[j][i], temp)
            yz += temp

        return xy + xz + yz
    
# Optimized solution
class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        xy = sum(1 for row in grid for val in row if val > 0)
        xz = sum(max(row) for row in grid)
        yz = sum(max(col) for col in zip(*grid))

        return xy + xz + yz