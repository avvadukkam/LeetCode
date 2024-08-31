# Time Complexity: O(n3)
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        maxDiff = 0  
        maxNum = 0   

        for num in nums:
            ans = max(ans, maxDiff * num)
            maxDiff = max(maxDiff, maxNum - num)
            maxNum = max(maxNum, num)   

        return ans
    

# Time complexity: O(n)
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        maxDiff = 0  
        maxNum = 0   

        for num in nums:
            ans = max(ans, maxDiff * num)
            maxDiff = max(maxDiff, maxNum - num)
            maxNum = max(maxNum, num)   

        return ans