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
    
# Optimized
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        num_set = set(nums)

        for num in num_set:
            if num + diff in num_set and num + 2 * diff in num_set:
                count += 1
        return count