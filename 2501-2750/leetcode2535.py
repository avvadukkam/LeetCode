class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        eleSum = sum(nums)
        digitSum = 0
        
        for num in nums:
            while num > 0:
                digitSum += num % 10
                num //= 10
        
        return abs(eleSum - digitSum)