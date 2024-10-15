class Solution:
    def isPathCrossing(self, path: str) -> bool:
        current = (0,0)
        visited = set()
        visited.add(current)
        for i in path:
            x, y = current
            if i =='N':
                current = (x, y+1)
            elif i =='S':
                current = (x, y-1)
            elif i =='E':
                current = (x+1, y)
            else: # 'W'
                current = (x-1, y)

            if current in visited:
                return True
            visited.add(current)
        return False