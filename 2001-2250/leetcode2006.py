# O(n2)
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if abs(nums[i]-nums[j])==k:
                    count += 1
        return count
    

# O(n)

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = 0
        freq = defaultdict(int)

        for num in nums:
            count += (freq[num - k] + freq[num + k])
            freq[num] += 1
        return count