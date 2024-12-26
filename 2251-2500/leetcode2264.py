class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_int = ""
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                max_int = max(max_int, num[i:i+3])
        return max_int