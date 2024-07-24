class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=1
        while i<len(nums)-1:
            if nums[i-1] == nums[i] and nums[i]==nums[i+1]:
                nums.remove(nums[i])
            else:
                i+=1
        return i+1