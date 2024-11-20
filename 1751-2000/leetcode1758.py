class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
    
        pattern1 = ''.join(['0' if i % 2 == 0 else '1' for i in range(n)]) 
        pattern2 = ''.join(['1' if i % 2 == 0 else '0' for i in range(n)])
        
        count1 = sum(1 for i in range(n) if s[i] != pattern1[i])
        count2 = sum(1 for i in range(n) if s[i] != pattern2[i])
        
        return min(count1, count2)