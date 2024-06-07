class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)

        setB = set(bobSizes)

        for x in aliceSizes:
            y = (sumB - sumA + 2 * x) // 2 
            if y in setB:
                return [x,y]
        return []