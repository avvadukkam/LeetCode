class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minNum, maxNum = min(nums), max(nums)
        
        while minNum:
            maxNum, minNum = minNum, maxNum % minNum
        return maxNum
