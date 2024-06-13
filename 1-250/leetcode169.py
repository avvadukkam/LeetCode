class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        result = 0
        maxcount = 0
        for n in nums:
            count[n] = 1 + count.get(n,0)
            result = n if count[n] > maxcount else result
            maxcount = max(count[n], maxcount)
        return result