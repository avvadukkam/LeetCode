class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        s = list(s)
        i, j = 0, len(s) - 1
        
        while i < j:
            if s[i] in vow and s[j] in vow:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
            elif s[i] in vow:
                j -= 1
            else:
                i += 1
        
        return ''.join(s)