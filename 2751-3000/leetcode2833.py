class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = moves.count('L')
        r = moves.count('R')
        distance = 0
        for i in moves:
            if i == 'L':
                distance-=1
            elif i == 'R':
                distance+=1
            elif l>r:
                distance-=1
            elif r>l:
                distance+=1
            else:
                distance+=1
        return abs(distance)