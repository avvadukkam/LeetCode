class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cons = 0
        temp = []
        for i in range(0,len(nums)):
            if nums[i] == 1:
                max_cons += 1
            else:
                temp.append(max_cons)
                max_cons = 0
            temp.append(max_cons)
        return max(temp)