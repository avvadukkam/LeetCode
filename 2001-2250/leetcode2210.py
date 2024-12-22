class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        count = 0
        nums = [nums[i] for i in range(len(nums) - 1) if nums[i] != nums[i + 1]] + [nums[-1]]
        for i in range(1,len(nums)-1):
            if nums[i] != nums[i-1] or nums[i] != nums[i+1]:
                if nums[i-1] < nums[i] and nums[i] > nums[i+1]: # hill
                    count += 1
                elif nums[i-1] > nums[i] and nums[i] < nums[i+1]: #valley
                    count += 1
        return count
    

# Optimized
class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        nums = [nums[i] for i in range(len(nums) - 1) if nums[i] != nums[i + 1]] + [nums[-1]]
        
        count = 0
        
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] > nums[i + 1]:  # Hill
                count += 1
            elif nums[i - 1] > nums[i] < nums[i + 1]:  # Valley
                count += 1
                
        return count