class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = []
        for r in ranges:
            for i in range(r[0],r[1]+1):
                if i not in covered:
                    covered.append(i)
        
        for i in range(left, right+1):
            if i not in covered:
                return False
        return True