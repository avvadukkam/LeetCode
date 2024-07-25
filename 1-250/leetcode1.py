# First Method - Use this
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i
        return 

# Second Method
class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        num_set = set()

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_set:
                complement_index = nums.index(complement)
                return [complement_index, i]
            num_set.add(num)
        return []
