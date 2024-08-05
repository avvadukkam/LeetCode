class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_sum = float('inf')
        running_sum = 0

        for num in nums:
            running_sum += num
            min_sum = min(min_sum, running_sum)

        return max(1, 1 - min_sum)
