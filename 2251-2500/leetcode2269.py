class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        numS = str(num)
        for i in range(len(numS)-k+1):
            if int(numS[i:i+k])!=0 and num%int(numS[i:i+k]) == 0:
                count += 1
        return count