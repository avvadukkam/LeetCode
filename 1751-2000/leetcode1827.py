class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(1,len(nums)):
            diff = nums[i-1] - nums[i] + 1
            if diff > 0:
                nums[i] += diff
                count += diff        
        return count