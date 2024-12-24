class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = nums[0]
        for i in range(1,len(nums)):
            res = list(set(res) & set(nums[i]))
        return sorted(res)