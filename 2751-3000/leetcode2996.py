class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        _sum = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1] + 1:
                _sum += nums[i]
            else:
                break
        
        missing = _sum
        while missing in nums:
            missing += 1
            
        return missing  
            