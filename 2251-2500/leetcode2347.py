class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        res = {5:"Flush", 3:"Three of a Kind", 2:"Pair", 1:"High Card"}
        if suits.count(suits[0]) == 5:
            return res[5]
        if any(ranks.count(rank) > 2 for rank in set(ranks)):
            return res[3]
        if any(ranks.count(rank) == 2 for rank in set(ranks)):
            return res[2]
        else:
            return res[1]
        
# Optimized
class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if len(set(suits)) == 1:
            return "Flush"

        rank_counts = Counter(ranks)
        max_count = max(rank_counts.values())

        if max_count >= 3:
            return "Three of a Kind"
        elif max_count == 2:
            return "Pair"
        else:
            return "High Card"