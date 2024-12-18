class Solution:
    def countPoints(self, rings: str) -> int:
        count = 0
        rods = defaultdict(set)
        for i in range(0,len(rings),2):
            rods[rings[i+1]].add(rings[i])
            
        for value in rods.values():
            if value == {'R','G','B'}:
                count += 1
        return count