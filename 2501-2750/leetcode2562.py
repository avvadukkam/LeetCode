class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        concatenation = 0
        left = 0
        right = len(nums)-1
        
        while left < right:
            concatenation += int(str(nums[left]) + str(nums[right]))
            left += 1
            right -= 1

        if left == right:
            concatenation += nums[left]
            
        return concatenation
    
#OR

class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l, r, result = 0, len(nums) - 1, 0

        while l < r:
            cur_val = str(nums[l]) + str(nums[r])
            result += int(cur_val)
            l += 1
            r -= 1

        if l == r:
            result += nums[l]
        
        return result