class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        start = nums[0]
        
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]+1:
                if start == nums[i-1]:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{nums[i - 1]}")
                start = nums[i]
                
        if start == nums[-1]:
            res.append(str(start))
        else:
            res.append(f"{start}->{nums[-1]}")

        return res
    
# More Efficient Way
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        start = end = nums[0]
        
        for i in range(1, len(nums)):
            curr = nums[i]

            if curr == end + 1:
                end = curr
            else:
                result.append(f"{start}->{end}" if start != end else str(start))
                start = end = curr

        result.append(f"{start}->{end}" if start != end else str(start))
        
        return result