class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        totalSum = sum(arr)
        if totalSum % 3 != 0:
            return False
        partSum = totalSum // 3
        currentSum = 0
        partCount = 0
       
        for num in arr:
            currentSum += num
            if currentSum == partSum:
                partCount += 1
                currentSum = 0
        
        return partCount >= 3