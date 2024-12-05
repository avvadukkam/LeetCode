class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n-3):
            for j in range(i+1, n-2):
                for k in range(j+1, n-1):
                    sumD = nums[i] + nums[j] + nums[k]
                    if nums[i] + nums[j] + nums[k] in nums[k+1:]:
                        count += nums[k+1:].count(sumD)

        return count