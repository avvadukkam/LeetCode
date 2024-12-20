class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_list = []
        res = []

        for i in range(len(nums)):
            if key == nums[i]:
                key_list.append(i)
        
        for i in range(len(nums)):
            if any(abs(i - j) <= k for j in key_list):
                res.append(i)

        return res

# Optimized
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        key_list = [i for i, num in enumerate(nums) if num == key]
        
        res = []
        for i in range(len(nums)):
            if any(abs(i - j) <= k for j in key_list):
                res.append(i)
        
        return res