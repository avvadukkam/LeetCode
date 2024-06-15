class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        while nums:
            p1, p2 = nums.pop(), nums.pop()
            res += p2
        return res
        