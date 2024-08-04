class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        oddSum = 0
        for i in range(0, len(arr), 2):
            for j in range(0, len(arr)-i):
                oddSum += sum(arr[j:j+i+1])
        return oddSum