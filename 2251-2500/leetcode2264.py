class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_int = ""
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                max_int = max(max_int, num[i:i+3])
        return max_int
    
# OR
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        dic = ["999","888", "777", "666","555", "444", "333", "222", "111", "000"]
        for val in dic:
            if val in num:
                return val
        return ""
    
# One-liner
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        dic = ["999","888", "777", "666","555", "444", "333", "222", "111", "000"]
        return next((val for val in dic if val in num), "")
