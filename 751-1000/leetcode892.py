class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        surface_area = 0
        n = len(grid)

        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    surface_area += 2 + 4 * grid[i][j]  # Top and bottom faces
                    if i > 0:
                        surface_area -= min(grid[i][j], grid[i-1][j])*2 # Glueing with upper neighbor
                    if j > 0:
                        surface_area -= min(grid[i][j], grid[i][j-1])*2 # Glueing with left neighbor
                        
        return surface_area