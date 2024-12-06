# Brute Force # O(n^3)
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n-3):
            for j in range(i+1, n-2):
                for k in range(j+1, n-1):
                    sumD = nums[i] + nums[j] + nums[k]
                    if sumD in nums[k+1:]:
                        count += nums[k+1:].count(sumD)

        return count
    
# Optimized # O(n^2)
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        freq = defaultdict(int)
        
        for k in range(n - 1, 1, -1):
            freq[nums[k]] += 1
            for j in range(k - 1, 0, -1):
                for i in range(j - 1, -1, -1):
                    sumD = nums[i] + nums[j] + nums[k]
                    count += freq[sumD]
        
        return count