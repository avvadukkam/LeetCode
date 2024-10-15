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
    
## OR
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        current = (0,0)
        visited = set()
        visited.add(current)
        moves = {
            'N': (0, 1),
            'S': (0, -1),
            'E': (1, 0),
            'W': (-1, 0)
        }
        
        for direction in path:
            dx, dy = moves[direction]
            current = (current[0] + dx, current[1] + dy)

            if current in visited:
                return True
            visited.add(current)
        return False