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
