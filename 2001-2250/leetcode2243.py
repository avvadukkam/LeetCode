class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            nums = []
            for i in range(0,len(s),k):
                nums.append(s[i:i+k])
            s = ''
            for num in nums:
                temp = 0
                for i in num:
                    temp += int(i)
                s += str(temp)
        return s
    
## OR Simplified version of the above is given below

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            nums = [s[i:i+k] for i in range(0, len(s), k)]
            s = ''.join(str(sum(int(digit) for digit in num)) for num in nums)
        return s