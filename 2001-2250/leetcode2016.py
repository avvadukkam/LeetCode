# Brute Force
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        maxDiff = -1
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    maxDiff = max(maxDiff, nums[j] - nums[i])

        return maxDiff
    

# Optimized
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_value = nums[0]
        max_diff = -1

        for num in nums[1:]:
            if num > min_value:
                max_diff = max(max_diff, num - min_value)
            else:
                min_value = num
        
        return max_diff