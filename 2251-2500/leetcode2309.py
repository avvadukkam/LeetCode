class Solution:
    def greatestLetter(self, s: str) -> str:
        res = ''
        for c in s:
            if ord(c) > 95 and c.upper() in s:
                if res<c.lower():
                    res = c
        return res.upper()