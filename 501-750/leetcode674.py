class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        longest = 1
        current_length = 1
        if not nums:
            return 0
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                current_length += 1
                longest = max(longest, current_length)
            else:
                current_length = 1
        return longest
        