# Brute Force
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j] - nums[i] == diff:
                    if nums[j] + diff in nums:
                        count += 1
        return count
    
