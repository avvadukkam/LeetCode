class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0]
        currentsum = 0
        for i in nums:
            if currentsum<0:
                currentsum = 0
            currentsum +=i
            maxsub = max(maxsub, currentsum)
        return maxsub