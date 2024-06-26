class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        max_l, offset = 0, 1

        for i in range(len(s)):
            l, r = i, i
            while r < len(s) - 1 and s[l] == s[r+1]:
                r += 1
            
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if r+1 - l > offset:
                    offset, max_l = r+1-l, l
                r += 1
                l -= 1
        return s[max_l: max_l + offset]