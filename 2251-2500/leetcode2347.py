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
        
