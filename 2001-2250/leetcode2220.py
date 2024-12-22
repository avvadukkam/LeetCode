class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = bin(start)[2:]
        goal = bin(goal)[2:]
        
        if len(start) > len(goal):
            goal = '0' * (len(start)-len(goal)) + goal
        elif len(start) < len(goal):
            start = '0' * (len(goal)-len(start)) + start
        
        count = 0
        for i in range(len(start)):
            if goal[i] != start[i]:
                count += 1
                
        return count
    
