class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            maxG = max(gifts)
            indexG = gifts.index(maxG)
            gifts[indexG] = math.floor(math.sqrt(maxG))
        return sum(gifts)