class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        count = defaultdict(int)
        for i in range(len(nums)-1):
            if nums[i] == key:
                count[nums[i+1]] += 1
                
        return max(count, key=count.get)
    

# OR
class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        count = {}
        for i in range(len(nums)-1):
            if nums[i] == key:
                target = nums[i + 1]
                count[target] = count.get(target, 0) + 1
                
        return max(count, key=count.get)