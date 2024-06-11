class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        count = 0
        domino_counts = {}
        for domino in dominoes:
            sorted_domino = tuple(sorted(domino))
            if sorted_domino in domino_counts:
                count += domino_counts[sorted_domino]
                domino_counts[sorted_domino] += 1
            else:
                domino_counts[sorted_domino] = 1
            
        return count