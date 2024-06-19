class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        temp = []
        for i in nums:
            if i not in temp:
                temp.append(i)
        temp.sort(reverse=True)
        
        return (temp[2]) if len(temp) >= 3 else max(temp)