class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        _sum = nums[0]
        sums = []
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                _sum += nums[i]
            else:
                sums.append(_sum)
                _sum = nums[i]
        else:
            sums.append(_sum)
        return max(sums)