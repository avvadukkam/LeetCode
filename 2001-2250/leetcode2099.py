class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        temp = sorted(nums)[-k:]
        temp_counts = {num: temp.count(num) for num in temp}
        out = []
        for i in nums:
            if i in temp_counts and temp_counts[i] > 0:
                out.append(i)
                temp_counts[i] -= 1
        return out