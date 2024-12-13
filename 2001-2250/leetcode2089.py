class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                res.append(i)

        return res



# OR
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
       
        left = bisect_left(nums, target)  
        right = bisect_right(nums, target) 
        
        if left == right:
            return []
        
        return list(range(left, right))